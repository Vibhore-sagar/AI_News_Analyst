from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from app.models.analysis import SentimentScores
import logging

logger = logging.getLogger("ainews.analysis.sentiment")

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_text(self, text: str) -> SentimentScores:
        """Uses VADER to extract deterministic polarity scores."""
        if not text:
            return SentimentScores(positive=0.0, negative=0.0, neutral=0.0, compound=0.0, overall_tone="Neutral")

        scores = self.analyzer.polarity_scores(text)
        
        compound = scores.get('compound', 0.0)
        
        if compound >= 0.05:
            tone = "Positive"
        elif compound <= -0.05:
            tone = "Negative"
        else:
            tone = "Neutral"

        return SentimentScores(
            positive=scores.get('pos', 0.0),
            negative=scores.get('neg', 0.0),
            neutral=scores.get('neu', 0.0),
            compound=compound,
            overall_tone=tone
        )

sentiment_analyzer = SentimentAnalyzer()
