from app.services.fetchers.newsapi_fetcher import newsapi_fetcher
from app.services.processing.deduplicator import deduplicator
from app.services.processing.cleaner import cleaner
from app.services.processing.clusterer import clusterer
from app.services.analysis.insight_generator import insight_generator
from app.agents.analysis_agent import analysis_agent
from typing import List, Dict
import logging

logger = logging.getLogger("ainews.agents.research")

class ResearchAgent:
    async def investigate_topic(self, query: str, limit: int = 20) -> Dict:
        """The core Hackathon Macro-Pipeline: Fetch -> Clean -> Cluster -> Analyze -> Insights."""
        logger.info(f"Research Agent starting ML pipeline on: {query}")
        
        # 1. FETCH
        logger.info("Research Agent: Fetching live HTML and cleaning data...")
        articles = await newsapi_fetcher.fetch_articles(query=query, limit=limit)
        if not articles:
            return {"status": "no data found"}
            
        # 2. CLEAN & DEDUPLICATE
        raw_dicts = [a.model_dump() for a in articles]
        unique_articles = deduplicator.remove_exact_duplicates(raw_dicts)
        for art in unique_articles:
            art["content"] = cleaner.clean_article_content(art.get("content", ""))
            
        # 3. CLUSTER (KMeans + TF-IDF)
        logger.info("Analysis Agent: Structuring semantic clusters using local TF-IDF vectorization...")
        clusters = clusterer.cluster_articles(unique_articles)
        
        # 4. ANALYZE & GENERATE INSIGHTS per Cluster
        logger.info("Analysis Agent: Extracting raw VADER sentiment and extracting TextRank matrices...")
        final_report = {
            "topic": query,
            "total_articles": len(unique_articles),
            "topic_clusters": []
        }
        
        for cluster_id, cluster_arts in clusters.items():
            # Analyze each article individually using SpaCy/VADER/TextRank
            articles_data = []
            for art in cluster_arts:
                analysis = await analysis_agent.analyze_article(art["content"])
                art["analysis"] = analysis
                articles_data.append(art)
                
            # Aggregate Sub-Metrics for the Cluster
            avg_sentiment = sum([a["analysis"]["sentiment"]["compound"] for a in articles_data]) / len(articles_data) if articles_data else 0.0
            
            all_entities = []
            for a in articles_data:
                all_entities.extend(a["analysis"]["entities"]["persons"] + a["analysis"]["entities"]["organizations"])
                
            # Form cluster payload for the rule-based insights engine
            cluster_data = {
                "article_count": len(articles_data),
                "avg_sentiment": avg_sentiment,
                "entities": list(set(all_entities)),
                "keywords": query.split()
            }
            
            # 5. GENERATE RULE-BASED INSIGHTS
            logger.info(f"Report Agent: Firing deterministic Rule-Based Insights for Node {cluster_id + 1}...")
            cluster_insights = insight_generator.generate_insight(cluster_data)
            
            final_report["topic_clusters"].append({
                "cluster_number": cluster_id + 1,
                "articles_in_cluster": len(articles_data),
                "aggregate_sentiment": "Positive" if avg_sentiment >= 0.05 else ("Negative" if avg_sentiment <= -0.05 else "Mixed"),
                "insights": cluster_insights,
                "sources_represented": list(set([a["source"] for a in articles_data])),
                "top_articles": [
                    {
                        "source": a["source"],
                        "title": a.get("title", ""),
                        "url": a.get("url", "#"),
                        "published_at": a.get("published_at", "Just now"),
                        "summary": a["analysis"]["summary"],
                        "bias_flags": a["analysis"]["bias_flags"]
                    } for a in articles_data[:3]
                ]
            })
            
        return final_report

research_agent = ResearchAgent()
