from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    language: str
    confidence: float
    sentiment: str
    toxicity: dict
