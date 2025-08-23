from transformers import pipeline
from functools import lru_cache

# Model IDs
LANG_DET_MODEL = "papluca/xlm-roberta-base-language-detection"   # returns lang + score
SENTIMENT_MODEL = "cardiffnlp/twitter-xlm-roberta-base-sentiment"  # neg/neu/pos
XNLI_MODEL = "joeddav/xlm-roberta-large-xnli"                     # zero-shot intents
TOXICITY_MODEL = "unitary/toxic-bert"                             # English toxicity (run on EN text)

@lru_cache(maxsize=1)
def lang_detector():
    return pipeline("text-classification", model=LANG_DET_MODEL, top_k=None)

@lru_cache(maxsize=1)
def sentiment_analyzer():
    return pipeline("text-classification", model=SENTIMENT_MODEL, top_k=None)

@lru_cache(maxsize=1)
def zero_shot_classifier():
    return pipeline("zero-shot-classification", model=XNLI_MODEL)

@lru_cache(maxsize=1)
def toxicity_classifier():
    return pipeline("text-classification", model=TOXICITY_MODEL, top_k=None)
