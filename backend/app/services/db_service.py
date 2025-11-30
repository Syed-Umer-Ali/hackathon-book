from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.db import ChatSession, ChatMessage
import uuid

async def create_session(db: AsyncSession, user_id: str = None) -> ChatSession:
    session = ChatSession(user_id=user_id)
    db.add(session)
    await db.commit()
    await db.refresh(session)
    return session

async def get_session(db: AsyncSession, session_id: str) -> ChatSession:
    result = await db.execute(select(ChatSession).where(ChatSession.id == session_id))
    return result.scalars().first()

async def add_message(
    db: AsyncSession, 
    session_id: str, 
    role: str, 
    content: str, 
    context_page: str = None,
    selected_text: str = None
) -> ChatMessage:
    message = ChatMessage(
        session_id=session_id,
        role=role,
        content=content,
        context_page=context_page,
        selected_text=selected_text
    )
    db.add(message)
    await db.commit()
    await db.refresh(message)
    return message

async def get_history(db: AsyncSession, session_id: str):
    result = await db.execute(
        select(ChatMessage)
        .where(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at)
    )
    return result.scalars().all()
