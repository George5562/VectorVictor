from typing import List, Tuple, Dict, Optional, Any
import dspy
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional
import json
import os
from dataclasses import dataclass
import logging

# Configure DSPy with the new syntax
lm = dspy.LM('openai/gpt-4o-mini')
dspy.configure(lm=lm)

class RelationType(Enum):
    IMPLEMENTS = "implements"
    DEPENDS_ON = "depends_on"
    EXTENDS = "extends"
    RELATED_TO = "related_to"
    EXAMPLE_OF = "example_of"
    PREREQUISITE = "prerequisite"
    
    def to_json(self):
        return self.value

@dataclass
class Relationship:
    """Represents a relationship between two documents."""
    source_doc: str
    target_doc: str
    relationship_type: RelationType
    description: str
    
    def to_dict(self):
        return {
            "source_doc": self.source_doc,
            "target_doc": self.target_doc,
            "relationship_type": self.relationship_type.value,  # Convert enum to string
            "description": self.description
        }

@dataclass
class Document:
    path: str
    content: str
    metadata: Dict[str, Any]

class DocumentExtractor(dspy.Signature):
    """Extract structured information from technical documentation."""
    
    content: str = dspy.InputField()
    title: str = dspy.OutputField(desc="The main title or subject of the document")
    summary: str = dspy.OutputField(desc="A concise summary of the document")
    key_concepts: list[str] = dspy.OutputField(desc="List of key technical concepts discussed")
    code_examples: list[str] = dspy.OutputField(desc="List of code examples found in the document")
    dependencies: list[str] = dspy.OutputField(desc="List of dependencies or related systems")

class RelationshipExtractor(dspy.Signature):
    """Extract relationships between documents.
    
    Given two technical documents and their metadata, determine how they are related.
    Valid relationship types are:
    - IMPLEMENTS: One document implements functionality described in another
    - DEPENDS_ON: One document requires functionality from another
    - EXTENDS: One document extends or builds upon another
    - RELATED_TO: Documents are related but not in above ways
    - EXAMPLE_OF: One document provides examples of another
    - PREREQUISITE: One document must be understood before another
    """
    
    source_content: str = dspy.InputField(desc="Content of the source document")
    target_content: str = dspy.InputField(desc="Content of the target document")
    source_path: str = dspy.InputField(desc="Path of source document")
    target_path: str = dspy.InputField(desc="Path of target document")
    shared_sections_str: str = dspy.InputField(desc="Comma-separated list of shared sections")
    shared_topics_str: str = dspy.InputField(desc="Comma-separated list of shared topics")
    relationship_type: str = dspy.OutputField(desc="Type of relationship (IMPLEMENTS, DEPENDS_ON, EXTENDS, RELATED_TO, EXAMPLE_OF, PREREQUISITE)")
    relationship_description: str = dspy.OutputField(desc="Description of how the documents are related")

class DocumentAnalyzer:
    """Document analyzer using DSPy's structured extraction."""
    
    def __init__(self):
        """Initialize the document analyzer with DSPy signatures."""
        # Define extractors using Predict
        self.document_extractor = dspy.Predict(DocumentExtractor)
        self.relationship_extractor = dspy.Predict(RelationshipExtractor)

    def analyze_document(self, document: Document) -> Dict:
        """Analyze a document and extract key information."""
        try:
            # Call the predictor with the document content
            response = self.document_extractor(content=document.content)
            return {
                "title": response.title,
                "summary": response.summary,
                "key_concepts": response.key_concepts,
                "code_examples": response.code_examples,
                "dependencies": response.dependencies,
                "content": document.content
            }
        except Exception as e:
            print(f"Error in document analysis: {str(e)}")
            return {}

    def extract_relationships(self, source_doc: Document, target_doc: Document, shared_sections: List[str] = None, shared_topics: List[str] = None) -> List[Relationship]:
        """Extract relationships between two documents."""
        try:
            # Convert lists to comma-separated strings
            shared_sections_str = ",".join(shared_sections) if shared_sections else ""
            shared_topics_str = ",".join(shared_topics) if shared_topics else ""
            
            # Call the predictor with content and metadata
            response = self.relationship_extractor(
                source_content=source_doc.content[:1000],  # Limit content length
                target_content=target_doc.content[:1000],  # Limit content length
                source_path=source_doc.path,
                target_path=target_doc.path,
                shared_sections_str=shared_sections_str,
                shared_topics_str=shared_topics_str
            )
            
            # Convert response to Relationship object
            try:
                # Clean and normalize relationship type
                rel_type_str = response.relationship_type.strip().upper()
                if rel_type_str in [t.name for t in RelationType]:
                    rel_type = RelationType[rel_type_str]
                    return [Relationship(
                        source_doc=source_doc.path,
                        target_doc=target_doc.path,
                        relationship_type=rel_type,
                        description=response.relationship_description
                    )]
                else:
                    print(f"Invalid relationship type: {rel_type_str}")
                    return []
            except (ValueError, AttributeError) as e:
                print(f"Error converting relationship: {str(e)}")
                return []
            
        except Exception as e:
            print(f"Error in relationship extraction: {str(e)}")
            return []

class DocumentProcessor:
    """Generic documentation processor that extracts structure and relationships."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize processor with optional custom config."""
        self.config = self._load_config(config_path)
        self.docs = {
            "index": {
                "sections": {},
                "topics": {}
            },
            "documents": {}
        }
        self._init_dspy()
    
    def _load_config(self, config_path: Optional[str] = None) -> Dict:
        """Load configuration from file."""
        default_config = Path(__file__).parent.parent / "config" / "default_config.json"
        config_file = Path(config_path) if config_path else default_config
        
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Error loading config from {config_file}: {str(e)}")
            raise
    
    def _init_dspy(self):
        """Initialize DSPy with model configuration."""
        dspy.settings.configure(
            model=self.config["model_config"]["model"],
            temperature=self.config["model_config"]["temperature"]
        )
    
    def process_directory(self, directory: Path) -> None:
        """Process all markdown files in a directory."""
        try:
            md_files = list(directory.glob("**/*.md"))
            print(f"\nFound {len(md_files)} markdown files\n")
            
            print("Phase 1: Initial document scan\n")
            for file_path in md_files:
                doc_id = str(file_path.relative_to(directory))
                print(f"\nInitial scan of {doc_id}:")
                self._initial_scan(file_path, doc_id)
                print(f"Successfully processed {doc_id}")
            
            print(f"\nProcessed {len(md_files)} documents in initial scan\n")
            
            print("Phase 2: Deep analysis and content extraction\n")
            for file_path in md_files:
                doc_id = str(file_path.relative_to(directory))
                print(f"\nAnalyzing files {doc_id}...")
                self.process_document_deep(file_path, doc_id)
            
            print("\nPhase 3: Comprehensive Relationship Mapping\n")
            self._map_relationships()
            
        except Exception as e:
            logging.error(f"Error processing directory {directory}: {str(e)}")
            raise
    
    def _initial_scan(self, file_path: Path, doc_id: str) -> None:
        """Perform initial scan of document to extract basic metadata."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Initialize document structure
            self.docs["documents"][doc_id] = {
                "title": "",
                "sections": self._init_section_structure(),
                "topics": set(),
                "relationships": []
            }
            
        except Exception as e:
            logging.error(f"Error in initial scan of {file_path}: {str(e)}")
            raise
    
    def _init_section_structure(self) -> Dict:
        """Initialize section structure from config."""
        return {
            section_id: {
                "title": section_info["title"],
                "content": "",
                "subsections": []
            }
            for section_id, section_info in self.config["section_types"].items()
        }
    
    def process_document_deep(self, file_path: Path, doc_id: str) -> None:
        """Deep analysis of document content."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Initialize document structure
            doc_structure = {
                "title": "",
                "sections": self._init_section_structure(),
                "relationships": [],
                "topics": set()
            }
            
            current_section = "overview"
            current_subsection = None
            code_block = False
            current_code = []
            
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('```'):
                    if code_block:
                        if current_code:
                            code_content = "\n".join(current_code)
                            if current_subsection:
                                current_subsection["code_examples"].append({
                                    "language": self._detect_language(current_code[0].strip('`')),
                                    "code": code_content
                                })
                        current_code = []
                    code_block = not code_block
                    continue
                
                if code_block:
                    current_code.append(line)
                    continue
                
                if line.startswith('#'):
                    level = len(line.split()[0].strip('#'))
                    header = line.strip('# ').lower()
                    title = line.strip('# ')
                    
                    if level == 1:
                        current_section = self._detect_section_type(header)
                        doc_structure["sections"][current_section]["content"] = ""
                        current_subsection = None
                        doc_structure["topics"].add(title)
                        if not doc_structure["title"]:
                            doc_structure["title"] = title
                    
                    elif level == 2:
                        subsection = {
                            "title": title,
                            "content": "",
                            "code_examples": []
                        }
                        doc_structure["sections"][current_section]["subsections"].append(subsection)
                        current_subsection = subsection
                        doc_structure["topics"].add(title)
                        
                        if "next" in header and i > 0:
                            for prev_line in reversed(lines[:i]):
                                if prev_line.startswith('##'):
                                    prev_title = prev_line.strip('# ')
                                    doc_structure["relationships"].append({
                                        "type": "NEXT_TOPIC",
                                        "from": prev_title,
                                        "to": title
                                    })
                                    break
                else:
                    content_line = line.strip()
                    if content_line:
                        if current_subsection is not None:
                            current_subsection["content"] += line + "\n"
                        else:
                            doc_structure["sections"][current_section]["content"] += line + "\n"
            
            # Add implicit relationships
            self._add_implicit_relationships(doc_structure)
            
            # Store processed content
            self.docs["documents"][doc_id].update({
                "title": doc_structure["title"],
                "sections": doc_structure["sections"],
                "topics": list(doc_structure["topics"]),
                "relationships": doc_structure["relationships"]
            })
            
            # Update index
            self._update_index(doc_id, doc_structure)
            
        except Exception as e:
            logging.error(f"Error in deep analysis of {file_path}: {str(e)}")
            raise
    
    def _detect_section_type(self, header: str) -> str:
        """Detect section type from header using config keywords."""
        header_lower = header.lower()
        for section_id, section_info in self.config["section_types"].items():
            if any(keyword in header_lower for keyword in section_info["keywords"]):
                return section_id
        return "overview"
    
    def _detect_language(self, lang_hint: str) -> str:
        """Detect code language from hint using config."""
        lang_hint = lang_hint.lower()
        for language, hints in self.config["code_languages"].items():
            if any(hint in lang_hint for hint in hints):
                return language
        return "text"
    
    def _add_implicit_relationships(self, doc_structure: Dict) -> None:
        """Add implicit relationships between sections."""
        for section_name, section in doc_structure["sections"].items():
            subsections = section["subsections"]
            for i in range(len(subsections) - 1):
                doc_structure["relationships"].append({
                    "type": "NEXT_IN_SECTION",
                    "from": subsections[i]["title"],
                    "to": subsections[i + 1]["title"],
                    "section": section["title"]
                })
    
    def _update_index(self, doc_id: str, doc_structure: Dict) -> None:
        """Update the documentation index."""
        for topic in doc_structure["topics"]:
            if topic not in self.docs["index"]["topics"]:
                self.docs["index"]["topics"][topic] = []
            self.docs["index"]["topics"][topic].append(doc_id)
            
            if topic == doc_structure["title"]:
                if topic not in self.docs["index"]["sections"]:
                    self.docs["index"]["sections"][topic] = {
                        "title": topic,
                        "documents": []
                    }
                self.docs["index"]["sections"][topic]["documents"].append(doc_id)
    
    def _map_relationships(self) -> None:
        """Map relationships between documents using DSPy."""
        try:
            print("\nMapping relationships across documents...")
            for doc_id, doc in self.docs["documents"].items():
                print(f"\nProcessing relationships for {doc_id}...")
                
                # Use DSPy for relationship mapping
                predictor = dspy.ChainOfThought("Extract relationships between topics")
                for topic in doc["topics"]:
                    for other_doc_id, other_doc in self.docs["documents"].items():
                        if doc_id != other_doc_id:
                            for other_topic in other_doc["topics"]:
                                prompt = f"Analyze the relationship between '{topic}' and '{other_topic}'"
                                result = predictor(prompt)
                                if result and hasattr(result, 'relationship'):
                                    doc["relationships"].append({
                                        "type": result.relationship,
                                        "from": topic,
                                        "to": other_topic,
                                        "confidence": result.confidence
                                    })
        
        except Exception as e:
            logging.error(f"Error in relationship mapping: {str(e)}")
            raise
    
    def save_processed_docs(self, output_file: Path) -> None:
        """Save processed documentation to file."""
        try:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.docs, f, indent=2, default=list)
            print(f"\nSuccessfully saved processed documentation to: {output_file}")
        
        except Exception as e:
            logging.error(f"Error saving to {output_file}: {str(e)}")
            raise

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Process documentation files')
    parser.add_argument("--docs_dir", type=str, help="Directory containing documentation to process", required=True)
    parser.add_argument("--output", type=str, help="Output file path", required=True)
    parser.add_argument("--config", type=str, help="Optional custom config file path")
    args = parser.parse_args()
    
    try:
        processor = DocumentProcessor(config_path=args.config)
        processor.process_directory(Path(args.docs_dir))
        processor.save_processed_docs(Path(args.output))
        
        print("\nGenerated Documentation Structure:")
        print(json.dumps(processor.docs["index"], indent=2))
        
    except Exception as e:
        logging.error(f"Error processing documentation: {str(e)}")
        raise

if __name__ == "__main__":
    main()
