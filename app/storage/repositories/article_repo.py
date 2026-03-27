from typing import Optional, List
from app.storage.mongodb import get_db
import logging

logger = logging.getLogger("ainews.article_repo")

class ArticleRepository:
    def __init__(self):
        self.collection_name = "articles"

    @property
    def collection(self):
        return get_db()[self.collection_name]

    async def create_article(self, article: dict) -> str:
        result = await self.collection.insert_one(article)
        return str(result.inserted_id)

    async def get_article_by_hash(self, url_hash: str) -> Optional[dict]:
        return await self.collection.find_one({"url_hash": url_hash})

    async def get_unprocessed_articles(self, limit: int = 50) -> List[dict]:
        cursor = self.collection.find({"processed": False}).limit(limit)
        return await cursor.to_list(length=limit)

    async def mark_as_processed(self, url_hash: str):
        await self.collection.update_one(
            {"url_hash": url_hash},
            {"$set": {"processed": True}}
        )

article_repo = ArticleRepository()
