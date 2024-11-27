# VectorVictor 

*"What's your vector, Victor?"* - Now you'll know!

A documentation vectorization system that extracts, analyzes, and organizes technical documentation for semantic search and LLM consumption. VectorVictor transforms your docs into a searchable knowledge base with the power of GPT-4 and vector embeddings.

## Features

- **Flexible Documentation Extraction**: Support for both GitHub repositories and web-based documentation
- **Intelligent Analysis**: Uses GPT-4 for content understanding and summarization
- **Vector Search**: Semantic search using OpenAI's text-embedding-3-small model
- **DSPy Integration**: Structured information extraction using DSPy's ChainOfThought
- **Progress Tracking**: Resumable processing for large documentation sets

## Project Structure
```
doc_scraper/
├── scraped_docs/           # Raw scraped documentation
│   └── [project_name]/     # Documentation organized by project
├── llm_docs/              # LLM-optimized documentation
│   └── [project_name]/    # Project-specific processed docs
│       ├── index.json     # Document metadata and organization
│       ├── content.json   # Processed document content
│       ├── embeddings.json # Vector embeddings (JSON format)
│       └── embeddings.npz  # Compressed embeddings (NumPy format)
├── scraper.py            # Documentation scraper
├── doc_processor.py      # Content processor and analyzer
├── convert_embeddings.py # Embedding format converter
└── test_api.py          # API connection tester
```

## Setup

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Test your setup:
```bash
python test_api.py
```

## Usage Guide

### 1. Documentation Scraping

The scraper supports two types of documentation sources:

#### GitHub Documentation
```bash
python scraper.py --url https://github.com/username/repo/docs --project project_name
```

The scraper will:
1. Detect if the URL points to a GitHub docs directory
2. Clone the repository if needed
3. Extract markdown and other documentation files
4. Save raw content in `scraped_docs/[project_name]`

#### Web Documentation
```bash
python scraper.py --url https://docs.example.com --project project_name --content-selector "article" --link-selector "a"
```

Optional arguments:
- `--content-selector`: CSS selector for main content (default: "article")
- `--link-selector`: CSS selector for navigation links (default: "a")
- `--max-depth`: Maximum recursion depth for link following (default: 5)

### 2. Document Processing

The processor uses GPT-4 and DSPy to analyze documentation:

```bash
python doc_processor.py --project [project_name]
```

Processing steps:
1. Content extraction from scraped documents
2. Vector embedding generation using text-embedding-3-small
3. Content analysis using DSPy and GPT-4:
   - Document title extraction
   - Summary generation
   - Key concept identification
   - Code example extraction
   - Dependency analysis
   - Related topic identification
4. Progress tracking in `llm_docs/progress.json`
5. Index maintenance in `llm_docs/index.json`

### 3. Embedding Optimization

Convert JSON embeddings to compressed NumPy format:

```bash
python convert_embeddings.py --input llm_docs/[project_name]
```

This conversion:
1. Reduces storage size through compression
2. Enables memory-mapped file access
3. Improves loading speed and memory efficiency

### Working with Processed Documentation

Example of semantic search using the processed documentation:

```python
import json
import numpy as np
from openai import OpenAI
from pathlib import Path

def semantic_search(query: str, project_dir: str, top_k: int = 3):
    # Initialize OpenAI client
    client = OpenAI()
    
    # Generate query embedding
    query_embedding = client.embeddings.create(
        input=query,
        model="text-embedding-3-small"
    ).data[0].embedding
    
    # Load document content and metadata
    with open(Path(project_dir) / 'content.json') as f:
        content = json.load(f)
    
    # Load compressed embeddings
    embeddings = np.load(Path(project_dir) / 'embeddings.npz')
    
    # Calculate similarities
    similarities = {
        doc_id: np.dot(query_embedding, doc_embedding) 
        for doc_id, doc_embedding in embeddings.items()
    }
    
    # Get top matches
    top_matches = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:top_k]
    
    # Return results with content
    return [
        {
            'doc_id': doc_id,
            'similarity': score,
            'content': content[doc_id]['content'],
            'metadata': content[doc_id]['metadata']
        }
        for doc_id, score in top_matches
    ]
```

## How It Works

### 1. DSPy Integration

DSPy is used for structured information extraction through its ChainOfThought module:

```python
class DocumentAnalyzer:
    def __init__(self):
        self.analyze = dspy.ChainOfThought(
            "content -> title, summary, key_concepts, code_examples, dependencies, related_topics"
        )
```

This creates a chain that:
1. Takes documentation content as input
2. Uses GPT-4 to understand the content
3. Extracts structured information in a consistent format

### 2. Embedding Generation

The system uses OpenAI's text-embedding-3-small model for vector embeddings:

```python
def get_embedding(text: str) -> List[float]:
    client = openai.OpenAI()
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding
```

These embeddings enable:
1. Semantic similarity search
2. Content clustering
3. Related document finding

### 3. Progress Tracking

The system maintains processing state in two files:
- `progress.json`: Tracks processed files
- `index.json`: Maintains document organization

This enables:
1. Resumable processing for large documentation sets
2. Progress monitoring
3. Efficient updates of specific documents

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
