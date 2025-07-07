import streamlit as st
from bible_helper import fetch_verse
from explain_helper import explain_verse

st.set_page_config(page_title="Bible Verse Interpreter", layout="centered")
st.title("📜 Bible Verse Interpreter")

verse_ref = st.text_input("Enter Bible Verse (e.g., John 3:16):")

if st.button("Explain Verse"):
    if not verse_ref:
        st.error("Please provide a verse reference.")
    else:
        verse_text = fetch_verse(verse_ref)
        if verse_text:
            st.subheader("📖 Verse Text (KJV)")
            st.write(verse_text)

            with st.spinner("Generating explanation..."):
                explanation = explain_verse(verse_ref, verse_text)

            st.subheader("🧠 Detailed Explanation")
            st.write(explanation)
        else:
            st.error("Verse not found or API error.")
