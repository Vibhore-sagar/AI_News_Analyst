from typing import List, Dict
from collections import Counter
import logging

logger = logging.getLogger("ainews.analysis.trends")

class TrendDetector:
    def detect_trends(self, all_topics: List[List[str]]) -> Dict[str, int]:
        """Calculates exact topic frequency across a batch of articles."""
        flat_topics = [topic for sublist in all_topics for topic in sublist]
        topic_counts = Counter(flat_topics)
        return dict(topic_counts.most_common(10))

    def detect_spikes(self, current_counts: Dict[str, int], historical_counts: Dict[str, int]) -> List[str]:
        """Detects if a keyword is spiking compared to historical baseline."""
        spikes = []
        for topic, count in current_counts.items():
            hist_count = historical_counts.get(topic, 0)
            if hist_count == 0 and count >= 3:
                spikes.append(topic)
            elif hist_count > 0 and (count / hist_count) > 2.0:
                spikes.append(topic)
        return spikes

trend_detector = TrendDetector()
