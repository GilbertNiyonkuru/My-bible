import requests

BOOKS = {
    "genesis": "genesis", "exodus": "exodus", "leviticus": "leviticus",
    "numbers": "numbers", "deuteronomy": "deuteronomy", "joshua": "joshua",
    "judges": "judges", "ruth": "ruth", "1 samuel": "1-samuel", "2 samuel": "2-samuel",
    "1 kings": "1-kings", "2 kings": "2-kings", "1 chronicles": "1-chr", "2 chronicles": "2-chr",
    "ezra": "ezra", "nehemiah": "nehemiah", "esther": "esther", "job": "job", "psalms": "psalms",
    "proverbs": "proverbs", "ecclesiastes": "ecclesiastes", "song of solomon": "song-of-solomon",
    "isaiah": "isaiah", "jeremiah": "jeremiah", "lamentations": "lamentations", "ezekiel": "ezekiel",
    "daniel": "daniel", "hosea": "hosea", "joel": "joel", "amos": "amos", "obadiah": "obadiah",
    "jonah": "jonah", "micah": "micah", "nahum": "nahum", "habakkuk": "habakkuk", "zephaniah": "zephaniah",
    "haggai": "haggai", "zechariah": "zechariah", "malachi": "malachi",
    "matthew": "matthew", "mark": "mark", "luke": "luke", "john": "john", "acts": "acts",
    "romans": "romans", "1 corinthians": "1-corinthians", "2 corinthians": "2-corinthians",
    "galatians": "galatians", "ephesians": "ephesians", "philippians": "philippians",
    "colossians": "colossians", "1 thessalonians": "1-thessalonians", "2 thessalonians": "2-thessalonians",
    "1 timothy": "1-timothy", "2 timothy": "2-timothy", "titus": "titus", "philemon": "philemon",
    "hebrews": "hebrews", "james": "james", "1 peter": "1-peter", "2 peter": "2-peter",
    "1 john": "1-john", "2 john": "2-john", "3 john": "3-john", "jude": "jude", "revelation": "revelation"
}

def fetch_verse(ref, version="en-kjv"):
    try:
        book_chap, verse = ref.split(":")
        parts = book_chap.strip().rsplit(" ", 1)
        book_name = parts[0].lower()
        chapter = parts[1]
        book = BOOKS.get(book_name)
        if not book:
            return None
        url = f"https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/{version}/books/{book}/chapters/{chapter}/verses/{verse}.json"
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return data.get("text", "").strip()
    except Exception:
        return None
