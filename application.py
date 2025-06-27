import streamlit as st
from summarizerr import TextSummarizer

st.set_page_config(page_title="Text Summarizer", layout="centered")

# Page Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📝 AI Text Summarizer</h1>", unsafe_allow_html=True)
st.markdown("### Paste any long paragraph and get a short summary instantly!")

# Text Input
text_input = st.text_area("Enter your text here:", height=300)

# Button
if st.button("✨ Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Summarizing using T5..."):
            summarizer = TextSummarizer()
            summary = summarizer.summarize(text_input)
        st.success("✅ Summary:")
        st.markdown(f"**{summary}**")
