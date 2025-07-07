import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

SYSTEM_PROMPT = """You are a biblical scholar assistant.
When given a Bible verse, respond with:
1. Author of the book
2. Historical and cultural context
3. Author’s intended meaning
4. A clear interpretation for today
"""

def explain_verse(reference, verse_text):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"{SYSTEM_PROMPT}\n\nReference: {reference}\nVerse: \"{verse_text}\""
    response = model.generate_content(prompt)
    return response.text.strip()
