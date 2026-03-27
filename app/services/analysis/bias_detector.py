import re
from typing import List
import logging

logger = logging.getLogger("ainews.analysis.bias")

class BiasDetector:
    def __init__(self):
        # Basic lexicon of words that often indicate subjective framing or loaded language
        self.loaded_words = [
            "controversial", "scandal", "outrageous", "draconian", "radical",
            "extremist", "scheme", "alleged", "so-called", "claims", "demands",
            "refuses", "slams", "blasts", "destroys"
        ]

    def detect_bias(self, text: str) -> List[str]:
        """Scans for loaded language and subjective framing to flag potential bias."""
        flags = []
        if not text:
            return flags

        lower_text = text.lower()
        found_words = []
        
        for word in self.loaded_words:
            if re.search(r'\b' + re.escape(word) + r'\b', lower_text):
                found_words.append(word)
                
        if found_words:
            flags.append(f"Contains loaded language hinting at subjective framing: {', '.join(found_words)}")
            
        # Basic check for extreme punctuation
        if text.count("!") > 3:
            flags.append("High usage of exclamation marks implies sensationalism.")

        return flags

bias_detector = BiasDetector()
