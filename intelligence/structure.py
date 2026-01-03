from intelligence.emotion import detect_emotions

def infer_emotional_arc(lyrics: str) -> dict:
    """
    Infer how emotion evolves across the lyrics.
    """

    raw_sections = [s.strip() for s in lyrics.split("\n\n") if s.strip()]
    section_data = []
    dominant_scores = []

    for idx, section in enumerate(raw_sections, start=1):
        emotions = detect_emotions(section)
        dominant_emotion = max(emotions, key=emotions.get)
        intensity = emotions[dominant_emotion]

        section_data.append({
            "section": idx,
            "dominant_emotion": dominant_emotion,
            "intensity": round(intensity,3)
        })

        dominant_scores.append(intensity)

    arc = "flat"

    if len(dominant_scores) >= 2:
        if dominant_scores[-1] > dominant_scores[0] + 0.1:
            arc = "slow_rise"
        elif dominant_scores[-1] < dominant_scores[0] - 0.1:
            arc = "slow_decline"
        elif max(dominant_scores) - min(dominant_scores) > 2:
            arc = "wave"        
            

    return {
        "emotional_arc" : arc,
        "section_emotions" : section_data
    }