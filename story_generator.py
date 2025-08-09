import os
from dotenv import load_dotenv
from openai import OpenAI

# Load your Hugging Face API token from .env
load_dotenv()
HF_TOKEN = os.getenv("HF_API_KEY")

# Create OpenAI-compatible client for Hugging Face models
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

def generate_story(prompt):
    completion = client.chat.completions.create(
        model="microsoft/phi-4",  # You can swap to other Hugging Face chat models
        messages=[
            {
                "role": "system",
                "content": "You are a creative short story teller. Your stories should be engaging, concise, and vivid."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8,
        max_tokens=1000
    )

    return (completion.choices[0].message.content)