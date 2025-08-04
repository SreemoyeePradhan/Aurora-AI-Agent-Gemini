import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the generative AI client
genai.configure(api_key=api_key)

def list_available_models():
    print("📦 Available Gemini Models:\n")
    try:
        models = genai.list_models()
        for model in models:
            print(f"- Model ID: {model.name}")
            print(f"  Description: {model.description}")
            print(f"  Input Token Limit: {model.input_token_limit}")
            print(f"  Output Token Limit: {model.output_token_limit}")
            print(f"  Supported Generation Methods: {model.supported_generation_methods}")
            print()
    except Exception as e:
        print("❌ Error listing models:", e)

if __name__ == "__main__":
    list_available_models()
