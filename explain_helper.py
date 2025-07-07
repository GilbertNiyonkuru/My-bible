import streamlit as st
import google.generativeai as genai

# ✅ Configure Gemini with your API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 📜 System prompt to guide the AI
SYSTEM_PROMPT = """You are a biblical scholar assistant.
When given a Bible verse, respond with:
1. Author of the book
2. Historical and cultural context
3. Author’s intended meaning
4. A clear interpretation for today
"""

# ✅ Function to explain a Bible verse
def explain_verse(reference, verse_text):
    try:
        # 🧠 Load Gemini Pro model with system prompt
        model = genai.GenerativeModel(
            model_name="models/gemini-1.5-pro",  # Use gemini-1.5-flash if you want faster/cheaper
            system_instruction=SYSTEM_PROMPT
        )
        
        # 📤 Send prompt to Gemini
        prompt = f"Reference: {reference}\nVerse: \"{verse_text}\""
        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        # ⚠️ Friendly error message if quota or API error occurs
        return (
            "⚠️ Sorry, we couldn't generate the explanation right now.\n"
            "You may have exceeded your daily quota or there was a connection error.\n"
            f"**Error**: {str(e)}"
        )
