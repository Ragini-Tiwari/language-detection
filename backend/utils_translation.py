from transformers import pipeline
from functools import lru_cache
from typing import Optional

# Mapping non-English → English translation models
OPUS_MODELS_TO_EN = {
    "es": "Helsinki-NLP/opus-mt-es-en",
    "ja": "Helsinki-NLP/opus-mt-ja-en",
    "ko": "Helsinki-NLP/opus-mt-ko-en",
    "zh": "Helsinki-NLP/opus-mt-zh-en",
    "fr": "Helsinki-NLP/opus-mt-fr-en",
    "de": "Helsinki-NLP/opus-mt-de-en",
    "hi": "Helsinki-NLP/opus-mt-hi-en",
    "bn": "Helsinki-NLP/opus-mt-bn-en",
    "ta": "Helsinki-NLP/opus-mt-ta-en",
    "te": "Helsinki-NLP/opus-mt-te-en",
    "mr": "Helsinki-NLP/opus-mt-mr-en",
    "kn": "Helsinki-NLP/opus-mt-kn-en",
    "ml": "Helsinki-NLP/opus-mt-ml-en",
    "gu": "Helsinki-NLP/opus-mt-gu-en",
    "pa": "Helsinki-NLP/opus-mt-pa-en",
    "ur": "Helsinki-NLP/opus-mt-ur-en",
}

# Mapping English → target translation models
OPUS_MODELS_FROM_EN = {
    "ta": "Helsinki-NLP/opus-mt-en-ta",
    "hi": "Helsinki-NLP/opus-mt-en-hi",
    "bn": "Helsinki-NLP/opus-mt-en-bn",
    "te": "Helsinki-NLP/opus-mt-en-te",
    "mr": "Helsinki-NLP/opus-mt-en-mr",
    "kn": "Helsinki-NLP/opus-mt-en-kn",
    "ml": "Helsinki-NLP/opus-mt-en-ml",
    "gu": "Helsinki-NLP/opus-mt-en-gu",
    "pa": "Helsinki-NLP/opus-mt-en-pa",
    "ur": "Helsinki-NLP/opus-mt-en-ur",
    "fr": "Helsinki-NLP/opus-mt-en-fr",
    "de": "Helsinki-NLP/opus-mt-en-de",
    "es": "Helsinki-NLP/opus-mt-en-es",
    "ja": "Helsinki-NLP/opus-mt-en-ja",
    "ko": "Helsinki-NLP/opus-mt-en-ko",
    "zh": "Helsinki-NLP/opus-mt-en-zh",
}


@lru_cache(maxsize=64)
def _translator(model_id: str):
    """Load a translation pipeline with caching."""
    return pipeline("translation", model=model_id)


def translate_to_english(text: str, src_lang: str) -> str:
    """Translate from given source language → English."""
    model_id = OPUS_MODELS_TO_EN.get(src_lang.lower())
    if not model_id:
        # Fallback: return original if no mapping
        return text
    translator = _translator(model_id)
    return translator(text)[0]["translation_text"]


def translate_from_english(text: str, tgt_lang: Optional[str]) -> str:
    """Translate from English → target language."""
    if not tgt_lang:
        return ""
    model_id = OPUS_MODELS_FROM_EN.get(tgt_lang.lower())
    if not model_id:
        return ""
    translator = _translator(model_id)
    return translator(text)[0]["translation_text"]
