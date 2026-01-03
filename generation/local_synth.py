import numpy as np
from scipy.io.wavfile import write


def generate_music_from_intent(
    mood: str,
    tempo_bpm: tuple,
    energy_level: str,
    output_path: str = "outputs/generated.wav"
):
    """
    Generate simple instrumental music based on musical intent.
    """

    sample_rate = 44100
    duration = 12  

    t = np.linspace(0, duration, int(sample_rate * duration), False)

    signal = np.zeros_like(t)

    if mood == "melancholic":
        base_freq = 220  # A3
    elif mood == "tense":
        base_freq = 330
    else:
        base_freq = 440

    if energy_level == "low":
        amplitude = 0.3
        mod_depth = 0.1
    elif energy_level == "medium":
        amplitude = 0.5
        mod_depth = 0.3
    else:
        amplitude = 0.7
        mod_depth = 0.6

    
    chord_freqs = [
        [220, 261.63, 329.63], 
        [196, 246.94, 293.66],  
        [174.61, 220, 261.63],
        [196, 246.94, 293.66],  
    ]

    segment_length = len(t) // len(chord_freqs)

    for i, chord in enumerate(chord_freqs):
        start = i * segment_length
        end = start + segment_length
        for freq in chord:
            signal[start:end] += amplitude * np.sin(
                2 * np.pi * freq * t[start:end]
            )

    signal += 0.2 * np.sin(2 * np.pi * base_freq * 2 * t)

    write(output_path, sample_rate, signal.astype(np.float32))

    print(f"🎼 Local music generated at {output_path}")
