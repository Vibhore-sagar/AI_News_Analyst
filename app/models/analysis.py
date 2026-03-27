from pydantic import BaseModel
from typing import List, Optional

class ExtractedEntities(BaseModel):
    persons: List[str] = []
    organizations: List[str] = []
    locations: List[str] = []
    events: List[str] = []

class SentimentScores(BaseModel):
    positive: float
    negative: float
    neutral: float
    compound: float
    overall_tone: str  # "Positive", "Negative", "Neutral"

class ArticleAnalysis(BaseModel):
    entities: ExtractedEntities
    sentiment: SentimentScores
    bias_flags: List[str] = []
    key_topics: List[str] = []
    insights: List[str] = []
