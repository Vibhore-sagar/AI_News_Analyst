from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from pydantic import BaseModel
from typing import List

from app.services.fetchers.newsapi_fetcher import newsapi_fetcher
from app.services.processing.deduplicator import deduplicator
from app.services.processing.cleaner import cleaner
from app.storage.repositories.article_repo import article_repo
from app.models.article import ArticleInDB
from app.utils.helpers import generate_url_hash
import logging

logger = logging.getLogger("ainews.api.news")
router = APIRouter()

class FetchRequest(BaseModel):
    query: str
    limit: int = 20

@router.post("/fetch-news")
async def fetch_news(request: FetchRequest, background_tasks: BackgroundTasks):
    """Triggers the NewsAPI fetcher to ingest data based on a query."""
    articles = await newsapi_fetcher.fetch_articles(query=request.query, limit=request.limit)
    
    if not articles:
        raise HTTPException(status_code=404, detail="No articles found for that query.")
        
    article_dicts = [a.model_dump() for a in articles]
    unique_articles = deduplicator.remove_exact_duplicates(article_dicts)
    
    inserted_count = 0
    for art in unique_articles:
        h = generate_url_hash(art["url"])
        existing = await article_repo.get_article_by_hash(h)
        if not existing:
            art["content"] = cleaner.clean_article_content(art.get("content", ""))
            
            db_article = ArticleInDB(**art, url_hash=h)
            await article_repo.create_article(db_article.model_dump(by_alias=True, exclude_none=True))
            inserted_count += 1
            
    return {"message": f"Successfully fetched and ingested {inserted_count} new unique articles."}
