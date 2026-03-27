from typing import Optional, List
from app.storage.mongodb import get_db
import logging

logger = logging.getLogger("ainews.report_repo")

class ReportRepository:
    def __init__(self):
        self.collection_name = "reports"

    @property
    def collection(self):
        return get_db()[self.collection_name]

    async def save_report(self, report: dict) -> str:
        result = await self.collection.insert_one(report)
        return str(result.inserted_id)

    async def get_recent_reports(self, limit: int = 10) -> List[dict]:
        cursor = self.collection.find().sort("generated_at", -1).limit(limit)
        return await cursor.to_list(length=limit)

report_repo = ReportRepository()
