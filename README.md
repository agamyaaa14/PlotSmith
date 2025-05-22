![App Banner](images/ps1.png)
---
# 📝 PlotSmith: AI-Powered Short Story Generator

**PlotSmith** is a lightweight, genre-flexible story generator powered by large language models. Whether you're brainstorming ideas, writing creatively, or just having fun, PlotSmith delivers short, compelling story snippets from your prompt with ease.

---

## 📚 Features

-  Supports multiple genres (Mystery, Fantasy, Sci-Fi, Horror, Romance, Detective, Thriller, and more)
-  Input a custom story prompt
-  Generates coherent, short story paragraphs instantly
-  Beautiful UI with dark theme and logo integration
-  Powered by open-access LLMs via Hugging Face Inference API

---

## 🚀 Tech Stack

| Component        | Technology                        |
|------------------|-----------------------------------|
| UI               | Streamlit                         |
| Backend Model    | `HuggingFaceH4/zephyr-7b-beta`    |
| API              | Hugging Face Inference API        |
| Styling          | Custom CSS                        |
| Environment Vars | Python `dotenv`                   |
| Deployment       | Streamlit Community Cloud         |

---

## 📂 File Structure

```bash
PlotSmith/
├── .env                       # Hugging Face API key (keep this secret)
├── .gitignore
├── README.md
├── app.py                    # Main Streamlit web app
├── story_generator.py        # Logic for generating stories via API
├── assets/
│   ├── ps1.png               # Logo used in app
|   ├── ps2.png         
│   └── ps2-nobg.png       
├── requirements.txt          # Python dependencies
└── prompts_to_try.txt        # Example prompts for each genre
```
---
## 🌐 Live Demo

🔗 [Deployed App](https://plotsmith.streamlit.app/)

![logo](images/ps2.png)

---

## ✅ Future Improvements

- Save stories to PDF or text  
- Add user login and favorites  
- Custom tone/style selection (humorous, dark, poetic, etc.)

---

## 📌 Conclusion

PlotSmith blends storytelling and technology into a lightweight, creative assistant. Whether you're writing for fun, school, or brainstorming, it delivers bite-sized stories tailored to your imagination.
