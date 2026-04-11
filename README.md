# 📝 ArticleGen

A lightweight AI-powered blog article generator built with **Flask** and **LangChain**, using **Groq's ultra-fast LLM inference** under the hood. Enter any topic, and get a well-written blog article in seconds.

---

## 🧠 How It Works

ArticleGen uses the **LangChain** framework to orchestrate the AI pipeline:

- **`ChatPromptTemplate`** — Structures the conversation with a system prompt that instructs the model to act as a blog writer, and a human message that passes in your topic.
- **`ChatGroq`** — LangChain's integration with [Groq](https://groq.com/), giving access to blazing-fast inference on models like `llama-3.1-8b-instant`.
- **LangChain Expression Language (LCEL)** — The `prompt | llm` chain pattern connects the prompt template and the model in a clean, composable pipeline.

```
User Input (topic)
      ↓
ChatPromptTemplate  →  formats the prompt
      ↓
ChatGroq (llama-3.1-8b-instant)  →  generates the article
      ↓
Flask Response  →  displays the article in the browser
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ArticleGen.git
cd ArticleGen
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the root directory:

```env
GROQ_API_KEY="your_groq_api_key_here"
```

Get your free API key at [console.groq.com](https://console.groq.com/).

### 5. Run the app

```bash
python main.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🗂️ Project Structure

```
ArticleGen/
├── main.py               # Flask app + LangChain pipeline
├── requirements.txt      # Python dependencies
├── .env                  # API keys (never commit this)
├── templates/
│   └── index.html        # Frontend UI
└── static/
    └── css/
        └── output.css    # Tailwind CSS output
```

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| Web Framework | Flask |
| AI Orchestration | LangChain |
| LLM Provider | Groq (`llama-3.1-8b-instant`) |
| Environment Config | python-dotenv |
| Styling | Tailwind CSS |

---

## ⚙️ Requirements

- Python 3.10+
- A free [Groq API key](https://console.groq.com/)

---

## 📄 License

MIT License — feel free to use and modify.