#app.py
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your Gemini API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set page config
st.set_page_config(page_title="Gemini Chat", page_icon="🤖")

st.title("🌟Hello All! This is AURORA🌟")
st.markdown("I am your personal AI assistant. Ask me anything and watch me as I reply...")

# User input box
prompt = st.text_input("Enter your prompt:")

# Trigger response on submit
if st.button("Generate Response") and prompt:
    st.info("Generating response...")
    
    # Use Gemini's native streaming
    model = genai.GenerativeModel("models/gemini-2.5-pro")
    
    with st.spinner("Thinking..."):
        # Stream the output chunk-by-chunk
        response_stream = model.generate_content(prompt, stream=True)
        
        full_response = ""
        message_placeholder = st.empty()

        for chunk in response_stream:
            if chunk.text:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")  # typing cursor effect

        message_placeholder.markdown(full_response)  # Final cleanup
