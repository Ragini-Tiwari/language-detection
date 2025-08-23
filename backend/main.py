from fastapi import FastAPI
from models import AnalyzeRequest, AnalyzeResponse
from pipelines import lang_detector, sentiment_analyzer, toxicity_classifier

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_text(request: AnalyzeRequest):
    text = request.text

    # Language detection
    lang_result = lang_detector()(text)[0]
    language = lang_result["label"]
    confidence = float(lang_result["score"])

    # Sentiment
    sentiment_result = sentiment_analyzer()(text)[0]
    sentiment = sentiment_result["label"]

    # Toxicity
    toxicity_result = toxicity_classifier()(text)[0]
    toxicity = {"label": toxicity_result["label"], "score": float(toxicity_result["score"])}

    return {
        "language": language,
        "confidence": confidence,
        "sentiment": sentiment,
        "toxicity": toxicity
    }
