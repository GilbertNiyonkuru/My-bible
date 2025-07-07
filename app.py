import streamlit as st
from helper import explain_verse

st.title("Simple Bible Verse Explainer")

verse_text = st.text_area("Enter a Bible verse")

if st.button("Explain Verse"):
    if verse_text.strip():
        explanation = explain_verse(verse_text)
        st.markdown(explanation)
    else:
        st.warning("Please enter a Bible verse to explain.")
