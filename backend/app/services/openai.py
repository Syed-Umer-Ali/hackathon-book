from openai import AsyncOpenAI, OpenAI
from app.core.config import settings
from typing import AsyncGenerator

# Configure OpenAI clients to use Google Gemini via compatibility layer
aclient = AsyncOpenAI(
    api_key=settings.GEMINI_API_KEY,
    base_url=settings.OPENAI_BASE_URL
)

# Sync client for scripts
client = OpenAI(
    api_key=settings.GEMINI_API_KEY,
    base_url=settings.OPENAI_BASE_URL
)

# Gemini Embedding Model
EMBEDDING_MODEL = "text-embedding-004" 
# Gemini Chat Model (changed to models/gemini-2.5-flash as requested)
CHAT_MODEL = "models/gemini-2.5-flash"

async def get_embedding_async(text: str) -> list[float]:
    text = text.replace("\n", " ")
    response = await aclient.embeddings.create(
        input=[text],
        model=EMBEDDING_MODEL
    )
    return response.data[0].embedding

def get_embedding_sync(text: str) -> list[float]:
    text = text.replace("\n", " ")
    response = client.embeddings.create(
        input=[text],
        model=EMBEDDING_MODEL
    )
    return response.data[0].embedding

async def generate_response_stream(
    query: str, 
    context: str,
    model: str = CHAT_MODEL
) -> AsyncGenerator[str, None]:
    
    system_prompt = """You are a helpful teaching assistant for the 'Physical AI & Humanoid Robotics' textbook.
    
    Instructions:
    1. Answer the student's question using the provided TEXTBOOK CONTENT.
    2. If the user has selected text (SELECTED TEXT BY USER), prioritize explaining that specific text.
    3. If the answer is not explicitly in the context, try to answer generally based on your knowledge but mention it's not in the context.
    4. Keep answers concise, friendly, and educational.
    """

    user_prompt = f"""
    TEXTBOOK CONTENT:
    {context}
    
    STUDENT QUESTION: 
    {query}
    """

    # Print prompt for debugging (will show in server logs)
    print("--- LLM PROMPT ---")
    print(user_prompt[:500] + "...") 
    print("------------------")

    stream = await aclient.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        stream=True
    )

    async for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
