import os
import json
import time
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TailwindScraper:
    def __init__(self, base_url: str = "https://tailwindcss.com/docs"):
        self.base_url = base_url
        self.visited_urls = set()
        self.docs_structure = {
            "categories": {},
            "pages": []
        }
        
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def normalize_url(self, url: str) -> str:
        """Normalize URL to prevent duplicates."""
        parsed = urlparse(url)
        path = parsed.path.rstrip('/')
        return f"{parsed.scheme}://{parsed.netloc}{path}"
    
    def is_valid_doc_url(self, url: str) -> bool:
        """Check if URL is a valid documentation page."""
        parsed = urlparse(url)
        return (
            parsed.netloc == urlparse(self.base_url).netloc and
            parsed.path.startswith("/docs") and
            not any(ext in parsed.path for ext in ['.png', '.jpg', '.gif', '.css', '.js'])
        )
    
    def get_page_content(self, url: str) -> dict:
        """Fetch and parse a documentation page using Selenium."""
        try:
            print(f"\nFetching: {url}")
            self.driver.get(url)
            
            # Wait for the main content to load
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))
            time.sleep(2)  # Extra time for dynamic content
            
            # Get the page source after JavaScript execution
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Extract main content
            main_content = soup.find('main')
            if not main_content:
                print(f"No main content found for {url}")
                return None
            
            # Extract title
            title = soup.find('h1')
            title_text = title.get_text().strip() if title else ""
            print(f"Found title: {title_text}")
            
            # Extract code examples
            code_blocks = []
            for code in main_content.find_all(['pre', 'code']):
                code_text = code.get_text().strip()
                if code_text:
                    code_blocks.append({
                        'language': code.get('class', [''])[0] if code.get('class') else '',
                        'code': code_text
                    })
            print(f"Found {len(code_blocks)} code examples")
            
            # Extract content sections
            sections = []
            current_section = {'title': '', 'content': ''}
            
            for elem in main_content.find_all(['h2', 'h3', 'p', 'ul', 'ol', 'div']):
                if elem.name in ['h2', 'h3']:
                    if current_section['content']:
                        sections.append(current_section.copy())
                    current_section = {
                        'title': elem.get_text().strip(),
                        'content': ''
                    }
                elif elem.name in ['p', 'ul', 'ol']:
                    text = elem.get_text().strip()
                    if text:
                        current_section['content'] += text + '\n\n'
            
            if current_section['content']:
                sections.append(current_section)
            
            print(f"Found {len(sections)} sections")
            
            # Create the page object
            page = {
                'url': url,
                'title': title_text,
                'sections': sections,
                'code_examples': code_blocks,
                'category': self._determine_category(url)
            }
            
            return page
            
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            return None
    
    def _determine_category(self, url: str) -> str:
        """Determine the category of a page based on its URL."""
        path = urlparse(url).path
        parts = path.split('/')
        if len(parts) > 2:
            return parts[2]
        return "general"
    
    def discover_links(self, url: str) -> list:
        """Discover all documentation links on a page using Selenium."""
        try:
            self.driver.get(url)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "nav")))
            time.sleep(2)  # Wait for dynamic content
            
            # Get all links from the navigation
            links = []
            elements = self.driver.find_elements(By.TAG_NAME, "a")
            
            for element in elements:
                try:
                    href = element.get_attribute('href')
                    if href:
                        full_url = urljoin(url, href)
                        normalized_url = self.normalize_url(full_url)
                        
                        if (
                            self.is_valid_doc_url(normalized_url) and 
                            normalized_url not in self.visited_urls
                        ):
                            print(f"Found link: {normalized_url}")
                            links.append(normalized_url)
                            self.visited_urls.add(normalized_url)
                except:
                    continue
            
            return links
            
        except Exception as e:
            print(f"Error discovering links on {url}: {str(e)}")
            return []
    
    def scrape(self, output_dir: str = "scraped_docs/tailwind"):
        """Scrape the entire documentation."""
        try:
            # Create output directory
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Start with the main docs page
            queue = [self.base_url]
            self.visited_urls.add(self.normalize_url(self.base_url))
            
            while queue:
                current_url = queue.pop(0)
                print(f"\nProcessing: {current_url}")
                
                # Get page content
                page = self.get_page_content(current_url)
                if page:
                    # Save page content
                    filename = f"{urlparse(current_url).path.replace('/', '_')}.md"
                    if filename.startswith('_'):
                        filename = filename[1:]
                    
                    file_path = output_path / filename
                    
                    # Convert page content to markdown
                    markdown_content = self._to_markdown(page)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                    print(f"Saved: {file_path}")
                    
                    self.docs_structure['pages'].append({
                        'url': current_url,
                        'title': page['title'],
                        'filename': filename,
                        'category': page['category']
                    })
                    
                    # Add category info
                    if page['category'] not in self.docs_structure['categories']:
                        self.docs_structure['categories'][page['category']] = []
                    self.docs_structure['categories'][page['category']].append(filename)
                
                # Discover new links
                new_links = self.discover_links(current_url)
                queue.extend([link for link in new_links if link not in self.visited_urls])
                print(f"Queue size: {len(queue)}")
            
            # Save documentation structure
            with open(output_path / 'structure.json', 'w', encoding='utf-8') as f:
                json.dump(self.docs_structure, f, indent=2)
            
        finally:
            self.driver.quit()
    
    def _to_markdown(self, page: dict) -> str:
        """Convert page content to markdown format."""
        markdown = f"# {page['title']}\n\n"
        
        # Add sections
        for section in page['sections']:
            if section['title']:
                markdown += f"## {section['title']}\n\n"
            markdown += f"{section['content']}\n\n"
        
        # Add code examples
        if page['code_examples']:
            markdown += "## Code Examples\n\n"
            for code in page['code_examples']:
                lang = code['language'] or 'text'
                markdown += f"```{lang}\n{code['code']}\n```\n\n"
        
        # Add source URL
        markdown += f"\nSource: {page['url']}\n"
        
        return markdown

def main():
    scraper = TailwindScraper()
    scraper.scrape()

if __name__ == "__main__":
    main()
