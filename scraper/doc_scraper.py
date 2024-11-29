"""Generic documentation scraper that can handle various documentation formats."""

import os
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import markdown

class DocumentationScraper:
    """A generic documentation scraper that can handle various formats."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize scraper with optional custom config."""
        self.config = self._load_config(config_path)
        self.driver = None
        self.output_dir = None
    
    def _load_config(self, config_path: Optional[str] = None) -> Dict:
        """Load configuration from file."""
        default_config = Path(__file__).parent.parent / "config" / "scraper_config.json"
        config_file = Path(config_path) if config_path else default_config
        
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Error loading config from {config_file}: {str(e)}")
            raise
    
    def setup_selenium(self):
        """Setup Selenium WebDriver."""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)
    
    def cleanup(self):
        """Clean up resources."""
        if self.driver:
            self.driver.quit()
    
    def scrape_documentation(self, url: str, output_dir: str) -> None:
        """Scrape documentation from a URL and save to output directory."""
        try:
            self.output_dir = Path(output_dir)
            self.output_dir.mkdir(parents=True, exist_ok=True)
            
            # Determine documentation type and use appropriate scraper
            if self._is_github_docs(url):
                self._scrape_github_docs(url)
            elif self._is_mkdocs(url):
                self._scrape_mkdocs(url)
            else:
                self._scrape_generic_docs(url)
            
            # Save structure
            self._save_structure()
            
        except Exception as e:
            logging.error(f"Error scraping documentation from {url}: {str(e)}")
            raise
        finally:
            self.cleanup()
    
    def _is_github_docs(self, url: str) -> bool:
        """Check if URL is a GitHub documentation."""
        return "github.com" in url
    
    def _is_mkdocs(self, url: str) -> bool:
        """Check if documentation is MkDocs based."""
        try:
            response = requests.get(url)
            return 'mkdocs' in response.text.lower()
        except:
            return False
    
    def _scrape_github_docs(self, url: str) -> None:
        """Scrape documentation from GitHub."""
        # Extract owner and repo from URL
        parts = url.split('/')
        owner = parts[-2]
        repo = parts[-1]
        
        # Use GitHub API to get documentation
        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/docs"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            files = response.json()
            for file in files:
                if file['name'].endswith('.md'):
                    content = requests.get(file['download_url']).text
                    self._save_markdown(file['name'], content)
    
    def _scrape_mkdocs(self, url: str) -> None:
        """Scrape MkDocs documentation."""
        if not self.driver:
            self.setup_selenium()
        
        self.driver.get(url)
        
        # Wait for navigation to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.md-nav'))
        )
        
        # Get all documentation links
        nav_items = self.driver.find_elements(By.CSS_SELECTOR, '.md-nav__link')
        links = [item.get_attribute('href') for item in nav_items if item.get_attribute('href')]
        
        # Process each page
        for link in links:
            self.driver.get(link)
            content = self.driver.find_element(By.CSS_SELECTOR, '.md-content').text
            filename = link.split('/')[-1].replace('.html', '.md')
            self._save_markdown(filename, content)
    
    def _scrape_generic_docs(self, url: str) -> None:
        """Scrape generic documentation website."""
        if not self.driver:
            self.setup_selenium()
        
        self.driver.get(url)
        
        # Wait for content to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        
        # Get all links
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        doc_links = [link.get_attribute('href') for link in links 
                    if link.get_attribute('href') and 
                    any(word in link.text.lower() for word in ['doc', 'guide', 'tutorial', 'api'])]
        
        # Process each page
        for link in doc_links:
            self.driver.get(link)
            content = self.driver.find_element(By.TAG_NAME, 'body').text
            filename = link.split('/')[-1].replace('.html', '.md')
            self._save_markdown(filename, content)
    
    def _save_markdown(self, filename: str, content: str) -> None:
        """Save content as markdown file."""
        if not filename.endswith('.md'):
            filename += '.md'
        
        output_path = self.output_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _save_structure(self) -> None:
        """Save documentation structure."""
        structure = {
            "files": [f.name for f in self.output_dir.glob('*.md')],
            "total_files": len(list(self.output_dir.glob('*.md')))
        }
        
        with open(self.output_dir / 'structure.json', 'w') as f:
            json.dump(structure, f, indent=2)

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape documentation from URL')
    parser.add_argument('--url', type=str, help='URL to scrape documentation from', required=True)
    parser.add_argument('--output', type=str, help='Output directory', required=True)
    parser.add_argument('--config', type=str, help='Optional custom config file')
    args = parser.parse_args()
    
    try:
        scraper = DocumentationScraper(config_path=args.config)
        scraper.scrape_documentation(args.url, args.output)
        print(f"Successfully scraped documentation to {args.output}")
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
