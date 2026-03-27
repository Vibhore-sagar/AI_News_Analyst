from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from app.core.settings import settings
from app.core.logging import logger
from app.storage.mongodb import connect_to_mongo, close_mongo_connection
from app.api.routes import news_routes
from app.api.routes import analysis_routes
from app.api.routes import report_routes
from app.jobs.scheduler import start_jobs

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Multi-agent intelligence layer for processing, extracting, and reporting structured news insights.",
    version="1.0.0"
)

app.include_router(news_routes.router, prefix=f"{settings.API_V1_STR}/news", tags=["News Ingestion"])
app.include_router(analysis_routes.router, prefix=f"{settings.API_V1_STR}/analysis", tags=["Local Intelligence"])
app.include_router(report_routes.router, prefix=f"{settings.API_V1_STR}/reports", tags=["Report Generation"])

@app.on_event("startup")
async def startup_db_client():
    logger.info("Connecting to MongoDB...")
    await connect_to_mongo()
    start_jobs()

@app.on_event("shutdown")
async def shutdown_db_client():
    logger.info("Closing MongoDB connection...")
    close_mongo_connection()

# Mount the frontend directory at the root AFTER the API routes to prevent shadowing
frontend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend")
os.makedirs(frontend_path, exist_ok=True)
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
