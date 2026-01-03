def make_music_decision(emotions: dict, energy: dict, arc: dict) -> dict:
    """
    Convert emotion, energy, and arc signals into musical decisions.
    """
    fear = emotions.get("fear", 0)
    sadness = emotions.get("sadness", 0)
    joy = emotions.get("joy", 0)
    anger = emotions.get("anger", 0)

    if fear + sadness > 0.6:
        mood = "melancholic"
    elif joy > 0.5:
        mood = "bright"
    elif anger > 0.4:
        mood = "dark_intense"
    else:
        mood = "neutral_ambient"

    energy_level = energy["energy_level"]

    if energy_level == "low":
        tempo = (60, 75)
    elif energy_level == "medium":
        tempo = (80, 100)
    else:
        tempo = (110, 140)

    if mood == "melancholic":
        instruments = ["soft piano", "ambient pads", "light strings"]
    elif mood == "bright":
        instruments = ["acoustic guitar", "light drums", "warm synths"]
    elif mood == "dark_intense":
        instruments = ["distorted bass", "dark synths", "heavy drums"]
    else:
        instruments = ["ambient textures", "subtle piano"]

    arc_type = arc["emotional_arc"]

    if arc_type == "flat":
        structure = "minimal progression, no big drop"
    elif arc_type == "slow_rise":
        structure = "gradual build, layered entry"
    elif arc_type == "slow_decline":
        structure = "gradual fade, sparse ending"
    else:
        structure = "dynamic contrast between sections"

    prompt = (
        f"{mood} instrumental music, "
        f"{structure}, "
        f"tempo {tempo[0]} to {tempo[1]} BPM, "
        f"featuring {', '.join(instruments)}"
    )
 
    return {
        "mood": mood,
        "tempo_bpm": tempo,
        "instruments": instruments,
        "structure": structure,
        "generation_prompt": prompt
    }