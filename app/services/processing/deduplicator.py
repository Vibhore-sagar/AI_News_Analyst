from typing import List, Dict
from app.utils.helpers import generate_url_hash

class Deduplicator:
    def remove_exact_duplicates(self, articles: List[dict]) -> List[dict]:
        """Removes articles with identical URL hashes from a list."""
        seen = set()
        unique = []
        for a in articles:
            h = a.get("url_hash")
            if not h:
                h = generate_url_hash(a.get("url", ""))
            if h not in seen:
                seen.add(h)
                unique.append(a)
        return unique

deduplicator = Deduplicator()
