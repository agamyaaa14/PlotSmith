from story_generator import generate_story

genre = "Mystery"
prompt = "A woman vanishes after entering a mirror maze at the fair."
story = generate_story(genre, prompt)
print("📖 Your Story\n", story)
