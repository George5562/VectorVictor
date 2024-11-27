"""Command-line interface for VectorVictor."""

import argparse
import os
from pathlib import Path
from dotenv import load_dotenv

from .scraper import DocScraper
from .doc_processor import DocumentProcessor
from .convert_embeddings import convert_embeddings

def main():
    """Main CLI entrypoint."""
    parser = argparse.ArgumentParser(
        description="VectorVictor - Documentation vectorization system"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Scrape command
    scrape_parser = subparsers.add_parser("scrape", help="Scrape documentation")
    scrape_parser.add_argument("--url", required=True, help="URL to scrape")
    scrape_parser.add_argument("--project", required=True, help="Project name")
    scrape_parser.add_argument("--content-selector", default="article", help="CSS selector for content")
    scrape_parser.add_argument("--link-selector", default="a", help="CSS selector for links")
    
    # Process command
    process_parser = subparsers.add_parser("process", help="Process documentation")
    process_parser.add_argument("--project", required=True, help="Project name")
    
    # Convert command
    convert_parser = subparsers.add_parser("convert", help="Convert embeddings to compressed format")
    convert_parser.add_argument("--project", required=True, help="Project name")
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    
    if args.command == "scrape":
        scraper = DocScraper()
        scraper.scrape_documentation(args.url, args.project, args.content_selector, args.link_selector)
    
    elif args.command == "process":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("Error: OPENAI_API_KEY environment variable not found")
            return
        
        processor = DocumentProcessor(api_key, f"scraped_docs/{args.project}")
        processor.process_all()
    
    elif args.command == "convert":
        convert_embeddings(Path(f"llm_docs/{args.project}"))
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
