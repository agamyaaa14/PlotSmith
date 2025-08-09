import streamlit as st
from story_generator import generate_story
from PIL import Image
import time

# Load header image (logo with name and slogan)
header_img = Image.open("images/ps1.png")
icon = Image.open("images/ps2-nobg.png")

# Page config
st.set_page_config(page_title="PlotSmith - Short Story Generator", page_icon=icon, layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2B2E4A;
        color: white;
    }
    .stTextInput > div > input,
    .stSelectbox > div > div {
        background-color: white !important;
        color: black !important;
        border-radius: 6px !important;
    }
    .stButton > button {
        background-color: #6D7CFF;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 10px 20px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #3E426A;
    }
    .story-output {
        background: linear-gradient(135deg, #3e426a, #6D7CFF);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 16px;
        line-height: 1.6;
        white-space: pre-wrap;
    }
    .footer {
        margin-top: 25px;
        text-align: center;
        color: white;
        opacity: 0.7;
        font-size: 14px;
    }
    label[data-testid="stWidgetLabel"] {
        color: white !important;
        font-size: 30px !important;
        margin-bottom: 4px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Show top logo
st.image(header_img, use_container_width=True)

# Genre list
genre = st.selectbox("Select Genre", [
    "Mystery", "Fantasy", "Sci-Fi", "Adventure",
    "Horror", "Detective", "Romance", "Thriller"
])

# Prompt Input
user_prompt = st.text_input("Enter your story prompt", placeholder="E.g. A detective finds a strange letter inside a locked room.")

# Generate Story
if st.button("Generate Story"):
    if user_prompt.strip():
        with st.spinner("Generating your story..."):
            full_prompt = f"Write a {genre} short story based on the following idea:\n{user_prompt}"
            story = generate_story(full_prompt)
            time.sleep(1.3)

        story_box = st.empty()
        animated_text = ""
        for char in story:
            animated_text += char
            story_box.markdown(
                f'<div class="story-output"><strong>{genre} Story</strong><br><br>{animated_text}</div>',
                unsafe_allow_html=True
            )
            time.sleep(0.005)

        # Footer
        st.markdown('<div class="footer">Made with 🤍 using PlotSmith</div>', unsafe_allow_html=True)
    else:
        st.error("Please enter a prompt to generate a story.")
