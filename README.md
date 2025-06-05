# 🧠 FastAPI Text Sentiment Analyzer

A production-ready FastAPI app that performs sentiment analysis using the [CardiffNLP Twitter RoBERTa model](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment). It classifies input text into **Positive**, **Neutral**, or **Negative**, making it ideal for real-world applications like analyzing tweets, chats, or reviews.

---

## 🚀 Features

- ✅ FastAPI backend with Swagger docs
- ✅ Uses `cardiffnlp/twitter-roberta-base-sentiment` for 3-label classification
- ✅ Returns sentiment + confidence score
- ✅ Clean API interface at `/analyze/`
- ✅ Ready for deployment or local testing

---

## 🧪 API Example

**POST** `/analyze/`

Request:
```json
{
  "text": "I sleep at 9 pm."
}
```

Response:
```json
{
  "text": "I sleep at 9 pm.",
  "sentiment": "NEUTRAL",
  "confidence": 0.97
}
```

---

## ⚙️ How to Run Locally

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Start the server

```bash
uvicorn main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

for the Swagger UI.

---

## 📁 File Structure

```
fastapi-text-analyzer/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Tech Stack

- Python
- FastAPI
- Transformers (Hugging Face)
- Torch
- Uvicorn

---

## 📌 Model Used

- **CardiffNLP/twitter-roberta-base-sentiment**
  - Fine-tuned on 124M tweets
  - Supports POSITIVE / NEGATIVE / NEUTRAL
  - Robust against slang, emojis, and social media text

---

## 👨‍💻 Author

**Navyanth Kumar Reddy**  
📍 Based in USA  
🔗 [GitHub](https://github.com/NavyanthReddy) | [LinkedIn](https://linkedin.com/in/NavyanthReddy)

---

## 🌟 Star this repo if you found it useful!

```bash
git clone https://github.com/NavyanthReddy/fastapi-text-analyzer.git
cd fastapi-text-analyzer
uvicorn main:app --reload
```

---
