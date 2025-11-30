from qdrant_client import QdrantClient
from qdrant_client.http import models
from app.core.config import settings

client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY
)

COLLECTION_NAME = "textbook_chunks"

def init_collection():
    """Create collection if it doesn't exist and create payload indexes."""
    collections = client.get_collections()
    exists = any(c.name == COLLECTION_NAME for c in collections.collections)
    
    if not exists:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(
                size=768,  # Gemini text-embedding-004 size
                distance=models.Distance.COSINE
            )
        )
        print(f"Collection '{COLLECTION_NAME}' created with vector size 768 (Gemini).")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists.")

    # Create Payload Index for 'source_page'
    try:
        client.create_payload_index(
            collection_name=COLLECTION_NAME,
            field_name="source_page",
            field_schema=models.PayloadSchemaType.KEYWORD
        )
        print(f"Created payload index for 'source_page'.")
    except Exception as e:
        print(f"Index for 'source_page' might already exist or error: {e}")
