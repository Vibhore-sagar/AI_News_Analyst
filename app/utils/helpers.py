import hashlib

def generate_url_hash(url: str) -> str:
    """Generates a secure hash for a URL to be used as a unique identifier."""
    return hashlib.sha256(url.encode('utf-8')).hexdigest()
