from app.services.analysis.entity_extractor import entity_extractor
from app.services.analysis.sentiment_analyzer import sentiment_analyzer
from app.services.analysis.bias_detector import bias_detector
from app.services.analysis.summarizer import summarizer
import logging
from typing import Dict, Any

logger = logging.getLogger("ainews.agents.analysis")

class AnalysisAgent:
    async def analyze_article(self, text: str) -> Dict[str, Any]:
        """Runs the trio of localized non-LLM models to structure raw text.
        Replaces LLMs with TextRank, SpaCy, and Vader.
        """
        logger.info("Starting ML analysis pipeline on article...")
        
        entities = entity_extractor.extract_entities(text)
        sentiment = sentiment_analyzer.analyze_text(text)
        bias = bias_detector.detect_bias(text)
        summary = summarizer.summarize(text, num_sentences=2)
        
        return {
            "entities": entities.model_dump(),
            "sentiment": sentiment.model_dump(),
            "bias_flags": bias,
            "key_topics": entities.events + entities.organizations,
            "summary": summary
        }

analysis_agent = AnalysisAgent()
