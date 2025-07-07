import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """You are a biblical scholar assistant.
When I give a verse reference and verse text, respond with:

1. Author of the verse/book
2. Historical situation/context when the author wrote it
3. Intended meaning and application at the time
4. A clear, concise interpretation of the verse today.
"""

def explain_verse(ref, verse_text):
    prompt = f"Verse: {ref}\nText: {verse_text}\n\nExplain:"
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )
    return resp.choices[0].message.content.strip()
