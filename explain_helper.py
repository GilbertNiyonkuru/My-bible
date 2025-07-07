import streamlit as st
from openai import OpenAI

# Initialize OpenAI client using the API key from secrets
openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You are a biblical scholar assistant.
When given a Bible verse, please:
1. Highlight the important words or phrases in the verse.
2. Explain what each of these words or phrases means in a real-life, practical way.
Respond clearly and simply.
"""

def explain_verse(verse_text):
    try:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Verse: \"{verse_text}\""}
        ]

        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",  # Change model if needed
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
