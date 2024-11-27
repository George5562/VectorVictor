"""Convert JSON embeddings to compressed NumPy format for efficient storage and loading.

This script converts OpenAI embeddings stored in JSON format to a compressed NumPy .npz format,
which provides several benefits:
1. Significantly reduced file size through compression
2. Memory-mapped file access for large embedding sets
3. Fast loading and efficient memory usage
4. Native NumPy array operations for similarity search
"""

import json
import numpy as np
from pathlib import Path

def convert_embeddings(input_dir: Path):
    """Convert JSON embeddings to compressed NumPy format.
    
    Args:
        input_dir (Path): Directory containing embeddings.json file
        
    The function:
    1. Loads embeddings from JSON
    2. Converts to float32 NumPy arrays
    3. Saves in compressed .npz format
    4. Verifies the conversion
    5. Reports compression statistics
    """
    embeddings_path = input_dir / 'embeddings.json'
    output_path = input_dir / 'embeddings.npz'
    
    print(f"Converting embeddings in {input_dir}")
    
    # Load JSON embeddings
    with open(embeddings_path) as f:
        embeddings = json.load(f)
    
    # Convert to numpy arrays and compress
    compressed_embeddings = {
        k: np.array(v, dtype=np.float32) 
        for k, v in embeddings.items()
    }
    
    # Save compressed version
    np.savez_compressed(output_path, **compressed_embeddings)
    
    # Print size comparison
    original_size = embeddings_path.stat().st_size / 1024 / 1024
    compressed_size = output_path.stat().st_size / 1024 / 1024
    
    print(f"Original size: {original_size:.2f} MB")
    print(f"Compressed size: {compressed_size:.2f} MB")
    print(f"Compression ratio: {original_size/compressed_size:.2f}x")
    
    # Verify we can load it back
    with np.load(output_path, mmap_mode='r') as data:
        print(f"\nVerification:")
        print(f"Number of documents: {len(data.files)}")
        print(f"Embedding dimension: {data[data.files[0]].shape[0]}")

if __name__ == '__main__':
    convert_embeddings(Path('llm_docs/atlas'))
