import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure the SDK
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all models available to your account
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Model Name: {m.name}")