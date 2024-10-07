import numpy as np
import matplotlib.pyplot as plt

# Sinusoid parameters
amplitude = 1
frequency = 2  # Hz
duration = 1  # seconds
sampling_rate = 1000  # Hz

# Generate time axis
time = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)

# Create sinusoid
signal = amplitude * np.sin(2 * np.pi * frequency * time)

# Perform Fourier transform
spectrum = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), d=1/sampling_rate)

# Plot the spectrum
plt.plot(frequencies, np.abs(spectrum))
plt.title('Spectrum of a Sinusoid')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()