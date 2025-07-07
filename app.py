import streamlit as st
from bible_helper import fetch_verse
from explain_helper import explain_verse

st.set_page_config(page_title="Bible AI Interpreter", layout="centered")
st.title("📖 Bible Verse Interpreter")

verse_ref = st.text_input("Verse (e.g. John 3:16)")
version = st.selectbox("Translation",
    ["en-kjv", "en-niv", "en-esv", "en-asv"])

if st.button("Explain Verse"):
    if not verse_ref:
        st.error("Please enter a verse reference.")
    else:
        verse = fetch_verse(verse_ref, version)
        if verse:
            st.subheader("📘 Verse Text")
            st.write(verse)
            with st.spinner("Generating explanation…"):
                explanation = explain_verse(verse_ref, verse)
            st.subheader("🧠 Deep Explanation")
            st.write(explanation)
        else:
            st.error("Could not fetch that verse. Check the reference or try another translation.")
