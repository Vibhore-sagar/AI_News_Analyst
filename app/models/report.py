from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Any, Optional
from datetime import datetime

class ReportBase(BaseModel):
    topic: str
    total_articles: int
    generated_at: datetime = Field(default_factory=datetime.utcnow)
    topic_clusters: List[Dict[str, Any]]
    
class ReportInDB(ReportBase):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = Field(alias="_id", default=None)
