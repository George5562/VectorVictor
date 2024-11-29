import os
from pathlib import Path
from vector_victor.doc_processor import DocumentProcessor
import json
from dotenv import load_dotenv

def main():
    # Load OpenAI API key from .env
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        return

    # Initialize processor with test directory
    processor = DocumentProcessor(api_key=api_key, base_dir="test_docs")
    
    # Process the test directory
    processor.process_directory(Path("test_docs"))
    
    # Read and print the output
    with open("llm_docs/documentation.json", "r") as f:
        doc = json.load(f)
        print("\nGenerated Documentation Structure:")
        print(json.dumps(doc, indent=2))

if __name__ == "__main__":
    main()
