import streamlit as st
from bible_helper import fetch_verse
from explain_helper import explain_verse

st.set_page_config(page_title="Bible ChatGPT Explainer", layout="centered")
st.title("📖 Bible Verse Explainer with AI")

verse_ref = st.text_input("Enter verse (e.g. John 3:16)")
version = st.selectbox("Translation", ["en-kjv", "en-niv", "en-esv", "en-asv"])

if st.button("Explain"):
    if not verse_ref:
        st.error("Please enter a verse reference.")
    else:
        verse_text = fetch_verse(verse_ref, version)
        if verse_text:
            st.subheader("📘 Verse Text")
            st.write(verse_text)

            with st.spinner("Analyzing with ChatGPT..."):
                explanation = explain_verse(verse_ref, verse_text)

            st.subheader("🧠 Explanation")
            st.write(explanation)
        else:
            st.error("Could not find that verse. Try checking your spelling or format.")
