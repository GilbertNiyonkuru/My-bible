import streamlit as st
import openai

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

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
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

st.title("Simple Bible Verse Explainer")

verse_text = st.text_area("Enter a Bible verse")

if st.button("Explain Verse"):
    if verse_text.strip():
        explanation = explain_verse(verse_text)
        st.markdown(explanation)
    else:
        st.warning("Please enter a Bible verse to explain.")
