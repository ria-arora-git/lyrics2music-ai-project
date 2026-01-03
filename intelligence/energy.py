import re

def estimate_energy(lyrics: str) -> dict:
    """
    Estimate musical energy from lyrics using structural heuristics.
    Returns a normalized energy score and categorical level.
    """
    lines = [line.strip() for line in lyrics.split("\n") if line.strip()]

    if not lines:
        return {
            "energy_score": 0.0,
            "energy_level": "low"
        }

    words_per_line = [len(line.split()) for line in lines]
    average_line_length = sum(words_per_line) / len(words_per_line)
    line_length_penalty = min(1.0, average_line_length / 10)

    unique_lines = set(lines)
    repetition_ratio = 1 - (len(unique_lines) / len(lines))
    repetition_penalty = repetition_ratio

    punctuation_hits = len(re.findall(r"[!?]", lyrics))
    punctuation_boost = min(1.0, punctuation_hits/5)

    energy_score = (
    0.7 * punctuation_boost +
    0.3 * (1 - line_length_penalty) -
    0.4 * repetition_penalty
    )

    energy_score = round(max(0.0, min(1.0, energy_score)), 3)

    if energy_score < 0.5:
        level = "low"
    elif energy_score < 0.75:
        level = "medium"
    else:
        level = "high"

    return {
        "energy_score": energy_score,
        "energy_level": level
    }
