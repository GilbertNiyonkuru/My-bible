import streamlit as st
from helper import explain_verse

st.title("Bible Verse Explainer")

reference = st.text_input("Enter Bible Reference (e.g., John 3:16)")
verse_text = st.text_area("Enter Verse Text")

if st.button("Explain Verse"):
    if reference and verse_text:
        explanation = explain_verse(reference, verse_text)
        st.markdown(explanation)
    else:
        st.warning("Please enter both the reference and verse text.")
