from pydantic_settings import BaseSettings
from pydantic import ConfigDict, field_validator
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    OPENAI_BASE_URL: str = "https://generativelanguage.googleapis.com/v1beta/openai/"
    
    # Keep these for library compatibility or if user switches back
    OPENAI_API_KEY: str 
    
    QDRANT_URL: str
    QDRANT_API_KEY: str
    DATABASE_URL: str

    @field_validator("DATABASE_URL", mode="before")
    def assemble_db_connection(cls, v: str) -> str:
        if v.startswith("postgres://"):
            v = v.replace("postgres://", "postgresql+asyncpg://", 1)
        elif v.startswith("postgresql://") and "+asyncpg" not in v:
            v = v.replace("postgresql://", "postgresql+asyncpg://", 1)
            
        # Fix for asyncpg: remove unsupported query params
        if "?" in v:
            parsed = urlparse(v)
            query = parse_qs(parsed.query)
            
            # List of params to remove that asyncpg doesn't support but libpq does
            params_to_remove = ["sslmode", "channel_binding", "options"]
            
            for param in params_to_remove:
                if param in query:
                    del query[param]
            
            # Reconstruct URL
            new_query = urlencode(query, doseq=True)
            v = urlunparse((
                parsed.scheme,
                parsed.netloc,
                parsed.path,
                parsed.params,
                new_query,
                parsed.fragment
            ))
            
        return v

    model_config = ConfigDict(env_file=".env", extra="ignore")

settings = Settings()
