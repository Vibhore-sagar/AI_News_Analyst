from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI News Analyst Agent"
    API_V1_STR: str = "/api/v1"
    
    # MongoDB Connect
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "ainews"
    
    # API Keys
    NEWSAPI_KEY: str = ""
    
    # Chroma Config
    CHROMA_PERSIST_DIRECTORY: str = "chroma_db"
    
    class Config:
        env_file = ".env"

settings = Settings()
