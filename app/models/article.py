from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime

class ArticleBase(BaseModel):
    title: str
    content: str
    source: str
    url: str
    published_at: Optional[datetime] = None
    author: Optional[str] = None

class ArticleInDB(ArticleBase):
    model_config = ConfigDict(populate_by_name=True)
    
    id: Optional[str] = Field(alias="_id", default=None)
    url_hash: str
    ingested_at: datetime = Field(default_factory=datetime.utcnow)
    processed: bool = False

class ArticleProcessed(ArticleInDB):
    clean_content: str
    chunks: List[str] = []
