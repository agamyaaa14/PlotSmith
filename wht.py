import streamlit as st
import requests
import os

hf_token = os.getenv("HF_API_KEY")
if not hf_token:
    st.error("API token not set!")
else:
    headers = {"Authorization": f"Bearer {hf_token}"}
    payload = {
        "inputs": "Once upon a time,",
        "parameters": {"max_new_tokens": 50}
    }
    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/microsoft/phi-4",
            headers=headers,
            json=payload,
        )
        response.raise_for_status()
        data = response.json()
        st.write("Output:", data)
    except Exception as e:
        st.error(f"API call failed: {e}")
