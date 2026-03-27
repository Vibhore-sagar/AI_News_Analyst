from fastapi import APIRouter
from app.agents.research_agent import research_agent
import logging

logger = logging.getLogger("ainews.api.analysis")
router = APIRouter()

@router.post("/investigate-and-analyze")
async def investigate_and_analyze(query: str, limit: int = 5):
    """
    Triggers the entire pipeline from beginning to end:
    Fetch -> Clean -> Deduplicate -> Extract Entities -> Identify Bias -> Query Ollama -> Store in DB.
    """
    result = await research_agent.investigate_topic(query, limit)
    return result
