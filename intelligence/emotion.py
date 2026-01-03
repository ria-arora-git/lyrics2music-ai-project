from transformers import pipeline

_emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

def detect_emotions(lyrics: str) -> dict:
    """
    Takes lyrics text and returns emotion probability distribution.
    """
    results = _emotion_classifier(lyrics)[0]

    emotion_scores = {}
    for item in results:
        emotion_scores[item["label"].lower()] = round(item["score"], 3)

    return emotion_scores