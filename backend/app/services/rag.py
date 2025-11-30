from app.services.vector_store import client, COLLECTION_NAME
from app.services.openai import get_embedding_async
from app.models.schemas import Source
from qdrant_client.http import models
from typing import Optional

async def search_textbook(
    query: str, 
    limit: int = 3, 
    current_page: Optional[str] = None
) -> list[Source]:
    embedding = await get_embedding_async(query)
    
    sources = []
    seen_content = set()

    # 1. Context-specific search (if page provided)
    if current_page:
        # Use query_points instead of search
        context_results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=embedding,
            query_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="source_page",
                        match=models.MatchValue(value=current_page)
                    )
                ]
            ),
            limit=2
        ).points
        
        for hit in context_results:
            payload = hit.payload
            content = payload.get("content", "")
            if content not in seen_content:
                sources.append(Source(
                    content=content,
                    source_page=payload.get("source_page", ""),
                    header_path=payload.get("header_path", "")
                ))
                seen_content.add(content)

    # 2. Global search
    # Use query_points instead of search
    global_results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=limit
    ).points
    
    for hit in global_results:
        payload = hit.payload
        content = payload.get("content", "")
        if content not in seen_content:
            sources.append(Source(
                content=content,
                source_page=payload.get("source_page", ""),
                header_path=payload.get("header_path", "")
            ))
            seen_content.add(content)
            
    return sources[:5] # Return top unique results
