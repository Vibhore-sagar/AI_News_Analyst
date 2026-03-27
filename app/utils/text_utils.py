import re

def clean_html(raw_html: str) -> str:
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = clean_html(text)
    text = normalize_whitespace(text)
    return text
