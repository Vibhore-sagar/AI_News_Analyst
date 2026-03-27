import requests
from typing import List
from datetime import datetime
from app.core.settings import settings
from app.models.article import ArticleBase
import logging

logger = logging.getLogger("ainews.newsapi")

class NewsAPIFetcher:
    def __init__(self):
        self.api_key = settings.NEWSAPI_KEY
        self.base_url = "https://newsapi.org/v2/everything"

    async def fetch_articles(self, query: str, limit: int = 20) -> List[ArticleBase]:
        if not self.api_key:
            logger.warning("No NewsAPI key found, skipping fetch.")
            return []
            
        params = {
            "q": query,
            "apiKey": self.api_key,
            "pageSize": limit,
            "language": "en",
            "sortBy": "publishedAt"
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            articles = []
            for item in data.get("articles", []):
                if item.get("title") and item.get("url"):
                    pub_date = item.get("publishedAt")
                    dt = datetime.fromisoformat(pub_date.replace("Z", "+00:00")) if pub_date else datetime.utcnow()
                    
                    articles.append(ArticleBase(
                        title=item["title"],
                        content=item.get("content") or item.get("description") or "",
                        source=item.get("source", {}).get("name", "NewsAPI"),
                        url=item["url"],
                        published_at=dt,
                        author=item.get("author")
                    ))
            return articles
        except Exception as e:
            logger.error(f"Error fetching from NewsAPI: {e}")
            return []
            
newsapi_fetcher = NewsAPIFetcher()
