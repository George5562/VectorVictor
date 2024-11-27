from typing import List, Dict, Optional, Any
import dspy
import openai
from dataclasses import dataclass
import os
from pathlib import Path
from tqdm import tqdm
from datetime import datetime
import json

@dataclass
class Document:
    path: str
    content: str
    metadata: Dict[str, Any]

class DocumentAnalyzer:
    """Extract key technical information from documentation using DSPy and GPT-4.
    
    This analyzer uses DSPy's ChainOfThought to extract structured information from
    documentation text, including:
    - Document title
    - Summary
    - Key concepts
    - Code examples
    - Dependencies
    - Related topics
    """
    def __init__(self):
        super().__init__()
        self.analyze = dspy.ChainOfThought("content -> title, summary, key_concepts, code_examples, dependencies, related_topics")

    def forward(self, content: str) -> Dict[str, Any]:
        """Analyze document content and extract structured information"""
        try:
            result = self.analyze(content=content)
            return {
                "title": result.title,
                "summary": result.summary,
                "key_concepts": result.key_concepts,
                "code_examples": result.code_examples,
                "dependencies": result.dependencies,
                "related_topics": result.related_topics
            }
        except Exception as e:
            print(f"Error analyzing content: {str(e)}")
            return {}

class DocumentProcessor:
    """Process documentation files with advanced analysis and embedding generation.
    
    This processor handles:
    1. Document content extraction
    2. OpenAI text-embedding-3-small vector generation
    3. GPT-4 powered content analysis
    4. Progress tracking for large documentation sets
    5. Index maintenance for processed documents
    
    The processor maintains state in two files:
    - progress.json: Tracks which files have been processed
    - index.json: Stores document metadata and organization
    
    Args:
        api_key (str): OpenAI API key for embeddings and GPT-4
        base_dir (str): Base directory containing documentation to process
    """
    def __init__(self, api_key: str, base_dir: str):
        # Configure OpenAI
        self.api_key = api_key
        
        # Initialize DSPy with OpenAI
        dspy.configure(api_key=api_key)
        openai_lm = dspy.LM(model="gpt-4-0125-preview", api_key=api_key)
        dspy.settings.configure(lm=openai_lm)
        
        self.base_dir = base_dir
        self.analyzer = DocumentAnalyzer()
        self.progress_file = "llm_docs/progress.json"
        self.index_file = "llm_docs/index.json"
        
        # Create output directory if it doesn't exist
        os.makedirs("llm_docs", exist_ok=True)
        
        # Load or initialize progress tracking
        self.progress = self._load_progress()
        self.index = self._load_index()

    def get_embedding(self, text: str) -> List[float]:
        """Get embedding from text-embedding-3-small"""
        client = openai.OpenAI(api_key=self.api_key)
        response = client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding

    def process_document(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Process a single document"""
        try:
            print(f"\nProcessing {file_path.name}:")
            
            # Skip if already processed
            if str(file_path) in self.progress and self.progress[str(file_path)]:
                print("Already processed, skipping...")
                return None
            
            # Read file content
            print("- Reading file content...")
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Generate embeddings
            print("- Generating embeddings...")
            embeddings = self.get_embedding(content)
            
            # Analyze content with GPT
            print("- Analyzing content with GPT...")
            analysis = self.analyzer.forward(content)
            
            # Create document record
            doc = {
                "content": content,
                "embeddings": embeddings,
                "analysis": analysis,
                "processed_at": str(datetime.now())
            }
            
            # Update progress
            self.progress[str(file_path)] = True
            self._save_progress(self.progress)
            
            return doc
            
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            return None

    def process_directory(self, directory: Path):
        """Process all documents in the directory"""
        try:
            # Initialize index if needed
            if "documents" not in self.index:
                self.index["documents"] = {}
            
            # Process all files in directory
            for file_path in Path(directory).rglob("*"):
                if file_path.is_file() and file_path.suffix in ['.md', '.txt', '.rst']:
                    doc = self.process_document(file_path)
                    if doc:
                        self.index["documents"][str(file_path)] = doc
            
            # Save index
            self._save_index(self.index)
            
        except Exception as e:
            print(f"Error processing directory: {str(e)}")

    def _load_progress(self) -> Dict[str, bool]:
        """Load processing progress"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_progress(self, progress: Dict[str, bool]):
        """Save processing progress"""
        with open(self.progress_file, 'w') as f:
            json.dump(progress, f, indent=2)
    
    def _load_index(self) -> Dict[str, Any]:
        """Load document index"""
        if os.path.exists(self.index_file):
            with open(self.index_file, 'r') as f:
                return json.load(f)
        return {
            "documents": {},
            "metadata": {
                "total_files": 0,
                "processed_files": 0,
                "last_updated": None
            }
        }
    
    def _save_index(self, index: Dict[str, Any]):
        """Save document index"""
        with open(self.index_file, 'w') as f:
            json.dump(index, f, indent=2)

    def export_for_llm(self, output_dir: str = "llm_docs"):
        """Export processed documents in a format optimized for LLM consumption"""
        try:
            # Create output directory
            os.makedirs(output_dir, exist_ok=True)
            output_path = Path(output_dir)
            
            # Load the index
            index = self._load_index()
            
            # Prepare the export structure
            llm_index = {
                "metadata": {
                    "total_documents": len(index["documents"]),
                    "last_updated": str(datetime.now())
                },
                "documents": index["documents"]
            }
            
            # Save the main index
            with open(output_path / "llm_index.json", "w") as f:
                json.dump(llm_index, f, indent=2)
            
            # Save content
            with open(output_path / "content.json", "w") as f:
                json.dump(index["documents"], f, indent=2)
            
            # Create README with updated instructions
            readme_content = f"""# LLM Documentation Index

This directory contains processed documentation optimized for LLM semantic search.

## Structure
- `llm_index.json`: Main index file with all document metadata and embeddings
- `content.json`: Document content and metadata

## Statistics
- Total Documents: {len(index["documents"])}
- Last Updated: {datetime.now()}

## Usage with LLMs
1. Load document content from `content.json`
2. Access embeddings and metadata from `llm_index.json`
3. Use embeddings for semantic search and content for context
"""
            with open(output_path / "README.md", "w") as f:
                f.write(readme_content)
            
            print(f"Successfully exported documentation to {output_dir}/")
            
        except Exception as e:
            print(f"Error exporting documentation: {str(e)}")

def main():
    # Load OpenAI API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        return

    # Initialize processor
    processor = DocumentProcessor(api_key=api_key, base_dir="docs")
    
    # Process documentation
    processor.process_directory(Path("docs"))
    processor.export_for_llm()

if __name__ == "__main__":
    main()
