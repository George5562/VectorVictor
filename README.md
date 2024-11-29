# Vector Victor: Beyond Embeddings

*"What's your vector, Victor?"* - Now you'll know!

A documentation vectorization system that extracts, analyzes, and organizes technical documentation for semantic search and LLM consumption. VectorVictor transforms your docs into a searchable knowledge base with the power of GPT-4 and vector embeddings.

## Overview

Vector Victor is an intelligent documentation processing system that analyzes, extracts, and maps relationships across technical documentation sets. Unlike traditional embedding-based approaches, Vector Victor uses advanced LLM-based parsing combined with DSPy Chain-of-Thought reasoning to understand documentation structure and relationships at a deeper semantic level.

## Why No Vectors?

During our development, we discovered that traditional vector embeddings, while useful for simple similarity searches, often miss the nuanced relationships and hierarchical structure present in technical documentation. By leveraging DSPy's Chain-of-Thought capabilities and GPT-4's advanced reasoning, we can:

1. Extract meaningful section hierarchies
2. Identify complex relationships between concepts
3. Understand prerequisite knowledge chains
4. Map implementation patterns and examples
5. Generate more accurate documentation graphs

## Features

- **Flexible Documentation Extraction**: Support for both GitHub repositories and web-based documentation
- **Intelligent Analysis**: Uses GPT-4 for content understanding and summarization
- **Smart Documentation Processing**: Hierarchical section extraction, code example detection and categorization, relationship mapping between concepts, prerequisite chain identification, framework-specific pattern recognition
- **Relationship Types**: IMPLEMENTS, DEPENDS_ON, EXTENDS, RELATED_TO, EXAMPLE_OF, PREREQUISITE, NEXT_TOPIC, NEXT_IN_SECTION
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
│       ├── relationships.json # Relationship mapping
│       └── graph.json     # Documentation graph
├── scraper.py            # Documentation scraper
├── doc_processor.py      # Content processor and analyzer
├── relationship_extractor.py # Relationship mapping
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
2. Hierarchical section extraction
3. Relationship mapping between concepts
4. Prerequisite chain identification
5. Framework-specific pattern recognition
6. Progress tracking in `llm_docs/progress.json`
7. Index maintenance in `llm_docs/index.json`

### 3. Relationship Extraction

Extract relationships between concepts:

```bash
python relationship_extractor.py --input llm_docs/[project_name]
```

This extraction:

1. Maps connections between concepts
2. Identifies relationship types (IMPLEMENT, DEPENDS_ON, etc.)
3. Saves relationships in `llm_docs/relationships.json`

### Working with Processed Documentation

Example of using the processed documentation:

```python
import json
from pathlib import Path

def load_documentation(project_dir: str):
    # Load document content and metadata
    with open(Path(project_dir) / 'content.json') as f:
        content = json.load(f)
  
    # Load relationships
    with open(Path(project_dir) / 'relationships.json') as f:
        relationships = json.load(f)
  
    # Use the loaded data for further analysis or visualization
    return content, relationships
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

### 2. Relationship Mapping

The system uses DSPy's Chain-of-Thought reasoning to map connections between concepts:

```python
def map_relationships(content: str) -> List[Relationship]:
    client = dspy.ChainOfThought(
        "content -> relationships"
    )
    response = client.analyze(content)
    return response.data[0].relationships
```

These relationships enable:

1. Accurate documentation graphs
2. Contextual processing
3. Nuanced understanding of documentation structure

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
