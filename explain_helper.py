import streamlit as st
import openai

# Configure OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

SYSTEM_PROMPT = """You are a biblical scholar assistant.
When given a Bible verse, respond with:
1. Author of the book
2. Historical and cultural context
3. Author’s intended meaning
4. A clear interpretation for today
"""

def explain_verse(reference, verse_text):
    try:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Reference: {reference}\nVerse: \"{verse_text}\""}
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # or "gpt-4o" or "gpt-4" depending on your access
            messages=messages,
            max_tokens=500,
            temperature=0.7,
        )
        
        explanation = response['choices'][0]['message']['content'].strip()
        return explanation
    
    except Exception as e:
        return (
            "⚠️ Sorry, we couldn't generate the explanation right now.\n"
            "You may have exceeded your quota or there was a connection error.\n"
            f"**Error**: {str(e)}"
        )
