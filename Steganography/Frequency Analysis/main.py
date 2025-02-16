import librosa
import numpy as np

# Load the audio file
y, sr = librosa.load("flagged-waveform.WAV", sr=None)

# Define the window size (for 1 second of audio)
window_size = sr

# Split the audio into 1-second segments
segments = [y[i:i+window_size] for i in range(0, len(y), window_size)]

# Compute the FFT of each segment
fft_segments = [np.fft.fft(seg) for seg in segments]

# For each segment, you might look for the frequency bin with maximum magnitude,
# and then map that to a character or digit.
for seg in fft_segments:
    magnitudes = np.abs(seg)
    index_max = np.argmax(magnitudes)
    print("Max frequency bin index:", index_max)
