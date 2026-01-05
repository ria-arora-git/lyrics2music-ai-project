import numpy as np
from scipy.io.wavfile import write
from scipy.signal import butter, lfilter

def apply_envelope(signal, sample_rate):
    """
    Smooth fade-in and fade-out to avoid clicks
    """
    attack = int(0.05 * sample_rate)
    release = int(0.3 * sample_rate)

    envelope = np.ones_like(signal)
    envelope[:attack] = np.linspace(0, 1, attack)
    envelope[-release:] = np.linspace(1, 0, release)

    return signal * envelope


def lowpass(signal, cutoff, sr):
    """
    Remove harsh high frequencies
    """
    b, a = butter(4, cutoff / (sr / 2), btype="low")
    return lfilter(b, a, signal)

def generate_music_from_intent(
    mood: str,
    tempo_bpm: tuple,
    energy_level: str,
    output_path: str = "outputs/generated.wav"
):
    """
    Generate melancholic chord-based instrumental music.
    """

    print("🎼 Generating local instrumental music...")

    sample_rate = 44100
    duration = 30
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    base_freq = 220.0

    chords = [
        [0, 3, 7],    # i
        [5, 8, 12],   # iv
        [7, 10, 14],  # v
        [0, 3, 7]     # i
    ]

    signal = np.zeros_like(t)

    chord_duration = duration / len(chords)

    for i, chord in enumerate(chords):
        start = int(i * chord_duration * sample_rate)
        end = int((i + 1) * chord_duration * sample_rate)

        chord_t = t[: end - start]
        chord_signal = np.zeros_like(chord_t)

        for note in chord:
            freq = base_freq * (2 ** (note / 12))
            chord_signal += (
                0.6 * np.sin(2 * np.pi * freq * chord_t) +
                0.3 * np.sin(2 * np.pi * freq * 2 * chord_t) +
                0.1 * np.sin(2 * np.pi * freq * 3 * chord_t)
            )

        chord_signal /= len(chord)
        chord_signal = apply_envelope(chord_signal, sample_rate)

        signal[start:end] += chord_signal

    signal /= np.max(np.abs(signal))
    signal *= 0.8

    signal = lowpass(signal, cutoff=3000, sr=sample_rate)

    write(output_path, sample_rate, signal.astype(np.float32))

    print(f"✅ Music saved to {output_path}")
