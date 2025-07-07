import requests

# Complete book mapping: lowercase → book id
BOOKS = { 
    "genesis": "genesis", "exodus": "exodus", "leviticus": "leviticus",
    "numbers": "numbers", "deuteronomy": "deuteronomy", "joshua": "joshua",
    # ... include all books ...
    "matthew": "matthew", "mark": "mark", "luke": "luke", "john": "john",
    "acts": "acts", "romans": "romans", "1 corinthians": "1-corinthians",
    # ... up through Revelation ...
    "revelation": "revelation"
}

def fetch_verse(ref, version="en-kjv"):
    """Fetch a single verse via wldeh/bible-api"""
    try:
        book_chap, verse = ref.split(":")
        parts = book_chap.strip().rsplit(" ", 1)
        book_name = parts[0].lower()
        chapter = parts[1]
        book = BOOKS[book_name]
        url = f"https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/{version}/books/{book}/chapters/{chapter}/verses/{verse}.json"
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return data.get("text", "").strip()
    except Exception:
        return None
