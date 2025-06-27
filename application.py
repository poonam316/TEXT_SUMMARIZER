import streamlit as st
from summarizerr import TextSummarizer

# Set Streamlit page config
st.set_page_config(page_title="📝 AI Text Summarizer", page_icon="📝", layout="centered")

# Custom CSS to improve UI
st.markdown("""
    <style>
    .main {
        background-color: #1E1E1E;
        color: #ffffff;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    textarea {
        border: 2px solid #4CAF50 !important;
        border-radius: 10px !important;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        height: 3em;
        width: 100%;
        margin-top: 1rem;
    }
    .summary-box {
        background-color: #2E7D32;
        padding: 1rem;
        border-radius: 10px;
        color: white;
        font-size: 18px;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📝 AI Text Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Paste any long paragraph and get a short summary instantly!</h4>", unsafe_allow_html=True)

# Text Input Area
text_input = st.text_area("✏️ Enter your text here:", height=300)

# Summary Length Slider
summary_len = st.slider("🧭 Summary Length (max tokens):", min_value=50, max_value=200, value=120, step=10)

# Summarize Button
if st.button("✨ Summarize"):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text first.")
    else:
        with st.spinner("⏳ Summarizing..."):
            summarizer = TextSummarizer()
            summary = summarizer.summarize(text_input, max_length=summary_len)
        st.markdown('<div class="summary-box">✅ <strong>Summary:</strong><br>' + summary + '</div>', unsafe_allow_html=True)
