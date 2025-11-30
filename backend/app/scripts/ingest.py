import os
import sys
import glob
import re
import uuid
from pathlib import Path
from typing import List, Dict

# Add backend directory to path so we can import app modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.services.vector_store import client as qdrant_client, COLLECTION_NAME, init_collection
from app.services.openai import get_embedding_sync
from qdrant_client.http import models

DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../physical-ai-book/docs"))

def parse_markdown(file_path: str) -> List[Dict]:
    """
    Parse markdown file into chunks based on headers.
    Returns list of dicts with content and metadata.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    filename = os.path.basename(file_path)
    slug = "/" + os.path.relpath(file_path, DOCS_DIR).replace("\\", "/").replace(".md", "")
    
    # Simple splitting by headers (H1, H2, H3)
    # This is a heuristic. For better results, use a proper MD parser or LangChain.
    chunks = []
    lines = text.split('\n')
    current_header = "Introduction"
    current_chunk = []
    
    for line in lines:
        if line.startswith('#'):
            # Save previous chunk
            if current_chunk:
                content = "\n".join(current_chunk).strip()
                if content:
                    chunks.append({
                        "content": content,
                        "metadata": {
                            "source_page": slug,
                            "header_path": current_header,
                            "chapter": slug.split('/')[1] if '/' in slug else "root"
                        }
                    })
            
            # Start new chunk
            current_header = line.strip().lstrip('#').strip()
            current_chunk = [line] # Keep the header in the chunk context
        else:
            current_chunk.append(line)
            
    # Save last chunk
    if current_chunk:
        content = "\n".join(current_chunk).strip()
        if content:
            chunks.append({
                "content": content,
                "metadata": {
                    "source_page": slug,
                    "header_path": current_header,
                    "chapter": slug.split('/')[1] if '/' in slug else "root"
                }
            })
            
    return chunks

def ingest():
    print(f"Scanning docs in: {DOCS_DIR}")
    init_collection()
    
    files = glob.glob(f"{DOCS_DIR}/**/*.md", recursive=True)
    print(f"Found {len(files)} markdown files.")
    
    total_chunks = 0
    
    for file_path in files:
        print(f"Processing {os.path.basename(file_path)}...")
        chunks = parse_markdown(file_path)
        
        if not chunks:
            continue
            
        points = []
        for chunk in chunks:
            embedding = get_embedding_sync(chunk["content"])
            point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, chunk["content"] + chunk["metadata"]["source_page"]))
            
            points.append(models.PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "content": chunk["content"],
                    **chunk["metadata"]
                }
            ))
            
        if points:
            qdrant_client.upsert(
                collection_name=COLLECTION_NAME,
                points=points
            )
            total_chunks += len(points)
            
    print(f"Ingestion complete. Uploaded {total_chunks} chunks.")

if __name__ == "__main__":
    ingest()
