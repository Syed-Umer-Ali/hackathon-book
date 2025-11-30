from pydantic import BaseModel
from typing import Optional, List

class ChatRequest(BaseModel):
    session_id: str
    query: str
    current_page: Optional[str] = None
    selected_text: Optional[str] = None

class Source(BaseModel):
    content: str
    source_page: str
    header_path: str

class ChatResponse(BaseModel):
    response: str
    sources: List[Source] = []
