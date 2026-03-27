from newspaper import Article as NewspaperArticle
import logging

logger = logging.getLogger("ainews.scraper")

class ScraperFetcher:
    async def scrape_article(self, url: str) -> str:
        """Downloads and extracts the clean text content from a web page."""
        try:
            article = NewspaperArticle(url)
            article.download()
            article.parse()
            return article.text
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            return ""

scraper_fetcher = ScraperFetcher()
