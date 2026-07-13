import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.title("😊 Emotion Detection & Learning Support Engine")

user_input = st.text_area("Describe your learning problem")

if st.button("Get AI Support"):
    model = genai.GenerativeModel("gemini-3.5-flash")
    response = model.generate_content(
        f"A student says: {user_input}. Give supportive learning advice."
    )
    st.success(response.text)