import os
import json
import time
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
import subprocess
import platform
import sys

sys.setrecursionlimit(10000)  # Increase recursion limit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocScraper:
    """A versatile documentation scraper that can extract content from both GitHub repositories
    and web-based documentation sites. Supports JavaScript-rendered content through Selenium
    and falls back to requests for static content.
    
    Features:
    - Automatic GitHub docs detection and cloning
    - JavaScript-rendered content support
    - Rate-limited crawling
    - Recursive link following with depth control
    - Customizable content and link selectors
    - Progress tracking and resumable scraping
    
    Args:
        output_dir (str): Base directory where scraped documentation will be saved
    """
    def __init__(self, output_dir: str = "scraped_docs"):
        """Initialize the documentation scraper.
        
        Args:
            output_dir (str): Base directory for scraped documentation
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        # Configure Chrome options for Selenium
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Special handling for Mac ARM
        if platform.system() == "Darwin" and platform.machine() == "arm64":
            options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            logger.error(f"Failed to initialize Chrome driver: {e}")
            # Fallback to requests-only mode
            self.driver = None
            logger.warning("Running in requests-only mode (no JavaScript support)")
        
        self.visited_urls = set()
        self.max_depth = 5  # Limit recursion depth
    
    def is_github_docs(self, url: str) -> bool:
        """Check if the URL is a GitHub docs directory."""
        try:
            parsed = urlparse(url)
            return parsed.netloc == "github.com" and any(x in parsed.path for x in ["/docs", "/documentation", "/doc"])
        except:
            return False

    def get_github_repo_info(self, url: str) -> tuple:
        """Extract GitHub repository information from URL."""
        parts = url.split('github.com/')[1].split('/')
        owner = parts[0]
        repo = parts[1]
        path = '/'.join(parts[2:]) if len(parts) > 2 else ""
        return owner, repo, path
    
    def clone_github_docs(self, url: str, project_name: str) -> str:
        """Clone GitHub documentation directory.
        
        Args:
            url (str): GitHub repository URL
            project_name (str): Name of the project
            
        Returns:
            str: Path to cloned documentation
        """
        owner, repo, path = self.get_github_repo_info(url)
        project_dir = os.path.join(self.output_dir, project_name)
        
        # Clone the repository to a temporary directory
        temp_dir = os.path.join(self.output_dir, "_temp")
        os.makedirs(temp_dir, exist_ok=True)
        
        try:
            # Clone repository
            subprocess.run(["git", "clone", f"https://github.com/{owner}/{repo}.git"], 
                         cwd=temp_dir, check=True)
            
            repo_dir = os.path.join(temp_dir, repo)
            docs_dir = os.path.join(repo_dir, path) if path else repo_dir
            
            # Move docs to project directory
            os.makedirs(project_dir, exist_ok=True)
            subprocess.run(["cp", "-r", f"{docs_dir}/.", project_dir], check=True)
            
            # Create index.json
            index = {
                "metadata": {
                    "project": project_name,
                    "source": url,
                    "type": "github",
                    "cloned_at": time.strftime("%Y-%m-%d %H:%M:%S")
                },
                "documents": {}
            }
            
            # Index all markdown and text files
            for root, _, files in os.walk(project_dir):
                for file in files:
                    if file.endswith(('.md', '.txt', '.rst')):
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, project_dir)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        index["documents"][rel_path] = {
                            "content": content,
                            "path": rel_path,
                            "url": f"{url}/{rel_path}",
                            "processed_at": time.strftime("%Y-%m-%d %H:%M:%S")
                        }
            
            # Save index
            with open(os.path.join(project_dir, "index.json"), 'w') as f:
                json.dump(index, f, indent=2)
            
            # Cleanup
            subprocess.run(["rm", "-rf", temp_dir], check=True)
            
            return project_dir
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to clone repository: {e}")
            raise
    
    def scrape_web_docs(self, url: str, project_name: str, 
                       content_selector: str = "article",
                       link_selector: str = "a",
                       excluded_paths: List[str] = None) -> str:
        """Scrape documentation from a website.
        
        Args:
            url (str): Base URL of the documentation
            project_name (str): Name of the project
            content_selector (str): CSS selector for main content
            link_selector (str): CSS selector for navigation links
            excluded_paths (List[str]): URL paths to exclude
            
        Returns:
            str: Path to scraped documentation
        """
        project_dir = os.path.join(self.output_dir, "atlas")
        os.makedirs(project_dir, exist_ok=True)
        
        excluded_paths = excluded_paths or []
        self.visited_urls = set()  # Reset visited URLs
        docs_index = {
            "metadata": {
                "project": project_name,
                "source": url,
                "type": "web",
                "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S")
            },
            "documents": {}
        }
        
        def should_process_url(url: str, depth: int) -> bool:
            """Check if URL should be processed."""
            if depth > self.max_depth:
                return False
                
            parsed = urlparse(url)
            path = parsed.path.rstrip('/')
            base_parsed = urlparse(self.base_url)
            
            # Only process URLs from the same domain and section
            base_path = urlparse(self.base_url).path.split('/')[1:3]  # e.g. ['docs', 'atlas']
            url_path = parsed.path.split('/')[1:3]
            
            return (
                (parsed.netloc == base_parsed.netloc or not parsed.netloc) and
                url_path[:2] == base_path[:2] and  # Stay within the same documentation section
                not any(ex in path for ex in excluded_paths)
            )
        
        def clean_filename(url: str) -> str:
            """Create a clean filename from URL."""
            parsed = urlparse(url)
            path = parsed.path.strip('/')
            if not path:
                return "index.md"
            return f"{path.replace('/', '_')}.md"
        
        def process_page(page_url: str, depth: int = 0):
            """Process a single documentation page."""
            if page_url in self.visited_urls:
                return
                
            # Handle relative URLs
            if not urlparse(page_url).netloc:
                page_url = urljoin(self.base_url, page_url)
                
            if not should_process_url(page_url, depth):
                return
            
            self.visited_urls.add(page_url)
            logger.info(f"Processing: {page_url}")
            
            try:
                # Use Selenium for dynamic content if available
                if self.driver:
                    self.driver.get(page_url)
                    time.sleep(2)  # Wait for dynamic content
                    current_url = self.driver.current_url
                    page_source = self.driver.page_source
                else:
                    response = self.session.get(page_url, allow_redirects=True, timeout=10)
                    current_url = response.url
                    
                    if response.status_code == 404:
                        logger.warning(f"404 error for {page_url}")
                        return
                        
                    page_source = response.text
                
                soup = BeautifulSoup(page_source, 'html.parser')
                
                # Try multiple content selectors if the first one fails
                content_selectors = [
                    content_selector,
                    "article",
                    "main",
                    ".content",
                    "#content",
                    ".documentation",
                    "body"
                ]
                
                content_elem = None
                for selector in content_selectors:
                    content_elem = soup.select_one(selector)
                    if content_elem and len(content_elem.get_text(strip=True)) > 100:  # Ensure meaningful content
                        break
                
                if not content_elem:
                    logger.warning(f"No content found for {page_url}")
                    return
                
                # Clean content
                for tag in content_elem.find_all(['script', 'style', 'nav', 'footer', 'header']):
                    tag.decompose()
                
                # Extract title
                title = soup.title.string if soup.title else ""
                title = title.replace(" | MongoDB Documentation", "").strip()
                
                # Convert content to markdown
                content = f"# {title}\n\n"
                content += f"Source: {current_url}\n\n"
                
                # Process text and code blocks
                for elem in content_elem.children:
                    if isinstance(elem, str):
                        text = elem.strip()
                        if text:
                            content += f"{text}\n\n"
                    elif elem.name in ['pre', 'code']:
                        code = elem.get_text(strip=True)
                        content += f"\n```\n{code}\n```\n\n"
                    elif elem.name == 'p':
                        text = elem.get_text(separator=' ', strip=True)
                        content += f"{text}\n\n"
                    elif elem.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                        text = elem.get_text(strip=True)
                        level = int(elem.name[1])
                        content += f"{'#' * level} {text}\n\n"
                    else:
                        text = elem.get_text(separator=' ', strip=True)
                        if text:
                            content += f"{text}\n\n"
                
                # Save content to file
                filename = clean_filename(current_url)
                file_path = os.path.join(project_dir, filename)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Add to index
                docs_index["documents"][filename] = {
                    "title": title,
                    "content": content,
                    "path": filename,
                    "url": current_url,
                    "processed_at": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                
                # Find links
                for link in soup.select(link_selector):
                    href = link.get('href')
                    if href and not href.startswith(('#', 'mailto:', 'tel:')):
                        next_url = urljoin(current_url, href)
                        process_page(next_url, depth + 1)
                
            except Exception as e:
                logger.error(f"Error processing {page_url}: {e}")
                if hasattr(e, '__traceback__'):
                    import traceback
                    logger.error(traceback.format_exc())
        
        # Store base URL for relative link resolution
        self.base_url = url
        
        # Start scraping from base URL
        process_page(url)
        
        # Save index
        with open(os.path.join(project_dir, "index.json"), 'w') as f:
            json.dump(docs_index, f, indent=2)
        
        logger.info(f"Scraped {len(docs_index['documents'])} pages to {project_dir}")
        return project_dir
    
    def scrape(self, url: str, project_name: str, **kwargs) -> str:
        """Scrape documentation from either GitHub or a website.
        
        Args:
            url (str): URL to documentation
            project_name (str): Name of the project
            **kwargs: Additional arguments for web scraping
            
        Returns:
            str: Path to scraped documentation
        """
        if self.is_github_docs(url):
            logger.info(f"Detected GitHub docs, cloning from: {url}")
            return self.clone_github_docs(url, project_name)
        else:
            logger.info(f"Scraping web documentation from: {url}")
            return self.scrape_web_docs(url, project_name, **kwargs)
    
    def __del__(self):
        """Clean up Selenium driver."""
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Scrape documentation from GitHub or websites")
    parser.add_argument("--url", required=True, help="URL to documentation")
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--content-selector", default="article", 
                       help="CSS selector for main content (web scraping only)")
    parser.add_argument("--link-selector", default="a", 
                       help="CSS selector for navigation links (web scraping only)")
    
    args = parser.parse_args()
    
    scraper = DocScraper()
    output_dir = scraper.scrape(
        args.url,
        args.project,
        content_selector=args.content_selector,
        link_selector=args.link_selector
    )
    
    print(f"\nDocumentation scraped to: {output_dir}")
    print("You can now process the documentation using doc_processor.py")
