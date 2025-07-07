import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

SYSTEM_PROMPT = """You are a biblical scholar assistant.
When given a Bible verse, respond with:
1. Author of the book
2. Historical and cultural context
3. Author’s intended meaning
4. A clear interpretation for today
"""

def explain_verse(reference, verse_text):
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro",
                                  system_instruction=SYSTEM_PROMPT)
    response = model.generate_content(f"Reference: {reference}\nVerse: \"{verse_text}\"")
    return response.text.strip()
