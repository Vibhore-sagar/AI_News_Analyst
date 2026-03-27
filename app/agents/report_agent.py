from app.agents.research_agent import research_agent
from app.services.report_generator.text_report import text_report_generator
from app.services.report_generator.visual_report import visual_report_generator
from app.storage.repositories.report_repo import report_repo
from app.models.report import ReportInDB
from typing import Dict
import logging

logger = logging.getLogger("ainews.agents.reports")

class ReportAgent:
    async def generate_comprehensive_report(self, query: str, limit: int = 20) -> Dict:
        """
        Coordinates the Macro-Pipeline and formats it into final deliverables.
        """
        logger.info(f"Report Agent starting for query: {query}")
        
        # 1. Trigger the heavy Macro-Pipeline (Fetch -> Clean -> Cluster -> Analyze -> Generate)
        pipeline_output = await research_agent.investigate_topic(query=query, limit=limit)
        
        if pipeline_output.get("status") == "no data found":
            return {"error": "No news articles found to generate a report."}

        # 2. Save the structured aggregated report to MongoDB
        db_report = ReportInDB(**pipeline_output)
        report_id = await report_repo.save_report(db_report.model_dump(by_alias=True, exclude_none=True))
        
        # 3. Format visual components
        markdown_summary = text_report_generator.generate_markdown(pipeline_output)
        
        # Calculate gross sentiment
        pos, neg, neu = 0, 0, 0
        for cluster in pipeline_output.get("topic_clusters", []):
            s = cluster.get("aggregate_sentiment", "Neutral")
            if "Pos" in s: pos += 1
            elif "Neg" in s: neg += 1
            else: neu += 1
                
        ascii_chart = visual_report_generator.generate_ascii_chart(pos, neg, neu)
        
        return {
            "report_id": report_id,
            "markdown": markdown_summary,
            "visual_chart": ascii_chart,
            "raw_json": pipeline_output
        }

report_agent = ReportAgent()
