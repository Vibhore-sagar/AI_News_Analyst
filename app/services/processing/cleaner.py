from app.utils.text_utils import clean_text
import re

class TextCleaner:
    def clean_article_content(self, raw_content: str) -> str:
        """Removes boilerplate, HTML, and extra spaces from article strings."""
        if not raw_content:
            return ""
        
        # Strip simple HTML
        text = clean_text(raw_content)
        
        # Remove common news disclaimers (basic regex)
        disclaimers = [
            r"Click here to read more\.",
            r"Subscribe for full access\.",
            r"All rights reserved\.",
            r"\[\+\]"
        ]
        for d in disclaimers:
            text = re.sub(d, "", text, flags=re.IGNORECASE)
            
        return text.strip()

cleaner = TextCleaner()
