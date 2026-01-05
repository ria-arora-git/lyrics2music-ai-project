from lyrics_sample import LYRICS
from intelligence.emotion import detect_emotions
from intelligence.energy import estimate_energy
from intelligence.structure import infer_emotional_arc
from intelligence.decision import make_music_decision
from generation.local_synth import generate_music_from_intent

def main():
    print("Lyrics loaded successfully.\n")
    emotions = detect_emotions(LYRICS)
    energy = estimate_energy(LYRICS)
    arc = infer_emotional_arc(LYRICS)
    decision = make_music_decision(emotions, energy, arc)

    print("\nMusic Decision : ", decision)

    generate_music_from_intent(
        mood=decision["mood"],
        tempo_bpm=decision["tempo_bpm"],
        energy_level=energy["energy_level"]
    )

if __name__ == "__main__":
    main()
