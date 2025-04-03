import streamlit as st
import requests

st.set_page_config(page_title="AI 新聞摘要", layout="centered")
st.title("🔎 InsightAlpha 前端")

text = st.text_area("輸入一段新聞內容：", height=200)
if st.button("產生摘要") and text.strip():
    response = requests.get("https://YOUR_SUMMARY_SERVICE_URL/summarize", params={"text": text})
    st.subheader("📋 AI 摘要")
    st.write(response.json()["result"])
