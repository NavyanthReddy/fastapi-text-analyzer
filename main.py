from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import torch

app = FastAPI()

# Load model + tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Map model labels to words
label_map = {
    "LABEL_0": "NEGATIVE",
    "LABEL_1": "NEUTRAL",
    "LABEL_2": "POSITIVE"
}

class TextInput(BaseModel):
    text: str

@app.post("/analyze/")
def analyze_text(input: TextInput):
    result = sentiment_pipeline(input.text)[0]
    return {
        "text": input.text,
        "sentiment": label_map[result['label']],
        "confidence": round(result['score'], 2)
    }
