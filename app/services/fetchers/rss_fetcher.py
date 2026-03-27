import feedparser
from typing import List
from datetime import datetime
from app.models.article import ArticleBase
from time import mktime
import logging

logger = logging.getLogger("ainews.rss")

class RSSFetcher:
    async def fetch_articles(self, feed_url: str, limit: int = 10) -> List[ArticleBase]:
        articles = []
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:limit]:
                dt = datetime.utcnow()
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    dt = datetime.fromtimestamp(mktime(entry.published_parsed))

                articles.append(ArticleBase(
                    title=entry.get('title', ''),
                    content=entry.get('summary', '') or entry.get('description', ''),
                    source=feed.feed.get('title', 'RSS Feed'),
                    url=entry.get('link', ''),
                    published_at=dt,
                    author=entry.get('author')
                ))
            return articles
        except Exception as e:
            logger.error(f"Error parsing RSS {feed_url}: {e}")
            return []

rss_fetcher = RSSFetcher()
