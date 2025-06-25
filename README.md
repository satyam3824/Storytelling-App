🔗 Live App: [Story teller ](https://app-gemini-storyteller.streamlit.app/)



# Storytelling-App
# 🧙‍♂️ AI Storytelling App

Create magical and engaging short stories from any idea using the power of **Google Gemini AI** and an elegant **Streamlit web interface**.

<div align="center">
  <img src="https://img.shields.io/badge/Made%20with-Streamlit-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Powered%20by-Google%20Gemini-blueviolet?style=flat-square" />
</div>

---

## 📌 Features

- 🔐 **Secure login** with username & password
- ✍️ Enter any story prompt or idea
- 🤖 AI-generated stories using **Gemini 1.5 Flash**
- 🌐 Beautiful, responsive web UI with `Streamlit`
- ⚡ Fast local and cloud performance
- 🎯 Ideal for content creators, educators, and hobbyists

---

## 🚀 Demo

> 💡 Enter a prompt like:  
> _"A time-traveling elephant discovers an ancient mystery in the jungle."_

Result:  
> _"In the deepest part of the Sumatran jungle..."_ ✨ *(AI completes the story)*

---

## 📂 Folder Structure

```
Storytelling-App/
├── app.py
├── requirements.txt
└── .streamlit/
    └── secrets.toml
```

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/storytelling-app.git
cd storytelling-app
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup secrets

Create `.streamlit/secrets.toml` with:

```toml
[passwords]
demo = "demo123"

[api_key]
api_key = "your_actual_google_gemini_api_key"
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit==1.35.0
google-generativeai==0.5.4
```

---

## 🔒 Login Credentials (for demo)

| Username | Password  |
|----------|-----------|
| demo     | demo123   |

---

## 🧠 Powered By

- [Streamlit](https://streamlit.io/)
- [Google Gemini (Generative AI)](https://ai.google.dev)

---

## 👨‍💻 Author

**Satyam Kumar**  
📫 [LinkedIn](https://www.linkedin.com/in/your-profile)  
🧑‍💼 Available for freelance AI/automation projects

---

## 📃 License

This project is licensed under the MIT License.
