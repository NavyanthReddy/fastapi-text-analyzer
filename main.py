from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class TextInput(BaseModel):
    text: str

# Load model once
sentiment_analyzer = pipeline("sentiment-analysis")

@app.post("/analyze/")
def analyze_text(input: TextInput):
    result = sentiment_analyzer(input.text)[0]
    return {
        "text": input.text,
        "sentiment": result["label"],
        "confidence": round(result["score"], 2)
    }
