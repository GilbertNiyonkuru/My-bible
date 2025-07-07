import requests

BIBLE_API_URL = "https://biblebytopic.com/api/getversenkjv/{book}/{chapter}/{verse}"

BOOK_NAME_TO_NUMBER = {BOOK_NAME_TO_NUMBER = {
    "genesis": 1,
    "exodus": 2,
    "leviticus": 3,
    "numbers": 4,
    "deuteronomy": 5,
    # ...
    "matthew": 40,
    "mark": 41,
    "luke": 42,
    "john": 43,
    "acts": 44,
    "romans": 45,
    # ...
    "revelation": 66,
}

def fetch_verse(ref):
    """
    Retrieves verse text from Bible API.
    ref = "John 3:16"
    Returns verse text or None.
    """
    try:
        book, chapv = ref.split()
        chap, verse = chapv.split(":")
        book_number = BOOK_NAME_TO_NUMBER[book.lower()]
        url = BIBLE_API_URL.format(book=book_number, chapter=chap, verse=verse)
        res = requests.get(url)
        if res.status_code == 200:
            return res.json().get("text")
    except Exception:
        pass
    return None
