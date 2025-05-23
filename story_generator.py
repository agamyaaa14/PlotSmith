import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/microsoft/phi-4"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_story(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 250,
            "temperature": 0.8,
            "top_p": 0.95,
            "do_sample": True,
        }
    }
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        if isinstance(result, list):
            return result[0]["generated_text"].split("Story:")[-1].strip()
        else:
            return f"⚠️ API returned unexpected format: {result}"
    except Exception as e:
        print("❌ API error:", e)
        return "❌ Error generating story. Please check your token or try again later."
