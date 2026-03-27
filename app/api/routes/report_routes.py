from fastapi import APIRouter
from app.agents.report_agent import report_agent
from fastapi.responses import PlainTextResponse
import logging

logger = logging.getLogger("ainews.api.reports")
router = APIRouter()

@router.post("/generate-report")
async def generate_report(query: str, limit: int = 15):
    """
    Executes the entire Pure ML Intelligence chain and returns a structured JSON payload 
    along with Markdown and ASCII chart deliverables.
    """
    result = await report_agent.generate_comprehensive_report(query, limit)
    return result

@router.post("/generate-markdown-report", response_class=PlainTextResponse)
async def generate_markdown_report(query: str, limit: int = 15):
    """
    Executes the intelligence chain and returns pure Markdown text ideal for rendering in a UI.
    """
    result = await report_agent.generate_comprehensive_report(query, limit)
    if "error" in result:
        return result["error"]
        
    final_output = result["markdown"] + "\n\n" + result["visual_chart"]
    return final_output
