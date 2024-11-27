"""VectorVictor: Documentation vectorization system.

This package provides tools for scraping, processing, and vectorizing technical documentation
for semantic search and LLM consumption.
"""

__version__ = "0.1.0"

from .scraper import DocScraper
from .doc_processor import DocumentProcessor, DocumentAnalyzer
from .convert_embeddings import convert_embeddings

__all__ = [
    "DocScraper",
    "DocumentProcessor",
    "DocumentAnalyzer",
    "convert_embeddings",
]
