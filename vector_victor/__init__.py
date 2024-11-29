"""VectorVictor: Documentation vectorization system.

This package provides tools for scraping and processing technical documentation
for LLM consumption with intelligent relationship mapping.
"""

__version__ = "0.1.0"

from .scraper import DocScraper
from .doc_processor import DocumentProcessor, DocumentAnalyzer

__all__ = [
    "DocScraper",
    "DocumentProcessor",
    "DocumentAnalyzer",
]
