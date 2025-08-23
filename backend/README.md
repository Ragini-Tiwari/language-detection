### Try it in your browser
- Start the server, then open: http://localhost:8000/docs
- Use the **/analyze** endpoint with a sample payload:


{
"text": "வணக்கம், நான் ரீஃபண்ட் வேண்டும்.",
"intents": ["greeting", "request_refund", "support_request", "complaint"],
"target_lang": "hi"
}


You will get: language (ta), confidence, sentiment, top_intent (likely request_refund), toxicity_score, EN translation, and optional HI translation.