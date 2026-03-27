from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.agents.report_agent import report_agent
import logging

logger = logging.getLogger("ainews.jobs")
scheduler = AsyncIOScheduler()

async def hourly_tech_analysis_job():
    """Runs automatically every hour to compile a fresh trending report."""
    logger.info("Executing scheduled hourly ML Macro-Pipeline job for 'AI Regulation'")
    try:
        # Fires the entire NewsAPI -> TextRank -> KMeans -> TextBlob Pipeline headless
        result = await report_agent.generate_comprehensive_report("AI Regulation", limit=15)
        if "error" not in result:
            logger.info(f"Scheduled Job Success. Report ID: {result.get('report_id')}")
    except Exception as e:
        logger.error(f"Scheduled Job Failed: {e}")

def start_jobs():
    scheduler.add_job(hourly_tech_analysis_job, 'interval', hours=1)
    scheduler.start()
    logger.info("APScheduler background jobs started daemonized.")
