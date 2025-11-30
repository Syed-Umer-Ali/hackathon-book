from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.schemas import ChatRequest
from app.services.rag import search_textbook
from app.services.openai import generate_response_stream
from app.services.db_service import add_message, get_history, create_session, get_session
from app.db.session import get_db
import json

router = APIRouter()

@router.post("/message")
async def chat_message(request: ChatRequest, db: AsyncSession = Depends(get_db)):
    # 0. Ensure session exists
    session = await get_session(db, request.session_id)
    if request.session_id == "temp-session" or not session:
         session = await create_session(db)
    
    # Save User Message
    await add_message(
        db, 
        session_id=session.id,
        role="user", 
        content=request.query,
        context_page=request.current_page,
        selected_text=request.selected_text
    )

    # 1. Retrieve context
    print(f"Searching for query: {request.query}, Page: {request.current_page}")
    sources = await search_textbook(request.query, current_page=request.current_page)
    print(f"Found {len(sources)} sources.")
    
    context_parts = []
    if request.selected_text:
        context_parts.append(f"SELECTED TEXT BY USER:\n{request.selected_text}\n")
    
    if sources:
        context_parts.append("TEXTBOOK CONTENT:")
        context_parts.extend([s.content for s in sources])
        
    context = "\n\n".join(context_parts)

    # 2. Generate response (Stream)
    async def event_generator():
        full_response = ""
        try:
            async for chunk in generate_response_stream(request.query, context):
                full_response += chunk
                yield f"data: {json.dumps({'text': chunk})}\n\n"
        except Exception as e:
            print(f"Error generating response: {e}")
            yield f"data: {json.dumps({'text': ' [Error generating response]'})}\n\n"
            
        # Send sources
        source_data = [s.dict() for s in sources]
        yield f"data: {json.dumps({'sources': source_data})}\n\n"
        
        # Save Assistant Message
        if session:
            await add_message(db, session_id=session.id, role="assistant", content=full_response)
        
        # Send session ID update if we created a new one
        if request.session_id == "temp-session":
             yield f"data: {json.dumps({'session_id': session.id})}\n\n"

        yield "data: [DONE]\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

@router.get("/sessions/{session_id}/history")
async def get_chat_history(session_id: str, db: AsyncSession = Depends(get_db)):
    history = await get_history(db, session_id)
    return history