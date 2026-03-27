import logging
from typing import List, Dict

logger = logging.getLogger("ainews.analysis.rules")

class RuleBasedInsightGenerator:
    def generate_insight(self, cluster_data: Dict) -> List[str]:
        """
        Generates deterministic insights based on clustering statistics and keyword matching.
        Expects a dictionary containing aggregated article data for a cluster.
        """
        insights = []
        
        # Extract cluster properties
        article_count = cluster_data.get("article_count", 0)
        avg_sentiment = cluster_data.get("avg_sentiment", 0.0)
        entities = cluster_data.get("entities", [])
        keywords = cluster_data.get("keywords", [])
        
        # Rule 1: Volume Spikes
        if article_count > 5:
            insights.append("This topic is gaining significant attention and is trending globally.")
            
        # Rule 2: Sentiment Bias
        if avg_sentiment < -0.2:
            insights.append("Overall sentiment across sources is negative, indicating widespread concern or risk.")
        elif avg_sentiment > 0.2:
            insights.append("Overall sentiment is positive, indicating optimism or growth in this sector.")
        elif article_count >= 3 and abs(avg_sentiment) < 0.1:
            insights.append("Mixed sentiment across sources suggests uncertainty or highly debated perspectives.")

        # Rule 3: Entity Impact
        entity_lower = [e.lower() for e in entities]
        if any(gov in entity_lower for gov in ["government", "biden", "eu", "congress", "policy", "regulator"]):
            insights.append("Government/Regulatory involvement suggests direct policy-level impact.")
            
        # Rule 4: Keyword Matching
        kw_lower = [k.lower() for k in keywords]
        if "startup" in kw_lower or "startups" in kw_lower:
            insights.append("Startups are likely to be affected, potentially facing increased compliance burdens.")
        if any(m in kw_lower for m in ["market", "stock", "investor", "financial"]):
            insights.append("This development has direct implications for financial markets and investors.")
            
        if not insights:
            insights.append("Standard news coverage. No extreme deviations in sentiment or volume detected.")

        return insights

insight_generator = RuleBasedInsightGenerator()
