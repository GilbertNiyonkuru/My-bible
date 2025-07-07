import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM = """You are a biblical scholar assistant.
When given a verse reference and verse text, provide:
1. Author of the book
2. Historical/cultural situation behind it
3. Author’s intended meaning
4. A concise modern-day interpretation"""

def explain_verse(ref, verse_text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Verse: {ref}\nText: \"{verse_text}\""}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
