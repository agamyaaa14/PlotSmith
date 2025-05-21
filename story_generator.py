import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# ✅ Load API key
load_dotenv()
hf_token = os.getenv("HF_API_KEY")

# ✅ Use free-tier safe model (not Nebius)
client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=hf_token,
)

def generate_story(genre: str, user_prompt: str) -> str:
    try:
        system_instruction = (
            f"You are a short story writer. Write a very short and coherent story in the {genre} genre "
            f"based on the given prompt. Do not use bullet points. Reply only with the story."
        )

        user_input = f"Genre: {genre}\nPrompt: {user_prompt.strip()}"

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_input}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error: {e}"


# ✅ Test it directly
if __name__ == "__main__":
    genre = "Mystery"
    user_prompt = "A woman vanishes after entering a mirror maze at the fair."
    story = generate_story(genre, user_prompt)
    print("\n📖 Your Story\n", story)
