import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

SYSTEM = """You are a biblical scholar assistant.
When given a Bible verse, respond with:
1. Author of the book
2. Historical and cultural context
3. Author’s intended meaning
4. A clear interpretation for today
"""

def explain_verse(reference, verse_text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Reference: {reference}\nVerse: \"{verse_text}\""}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
