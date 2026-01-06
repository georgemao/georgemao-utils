import re
import unicodedata

def slugify(text: str) -> str:
    """
    Convert a string to a URL-friendly slug.
    """
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', text)

def truncate_string(text: str, max_length: int, suffix: str = '...') -> str:
    """
    Truncate a string to a specific length with an optional suffix.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + suffix
