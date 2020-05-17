# pyhon-inverse-spectrogram

Inverse spectogram for scipy.signal.spectrogram done for the human ears.

      >>> from scipy.io import wavfile
      >>> import scipy.signal as signal
      >>> import numpy as np

      >>> fs, data = wavfile.read('./test_sound.wav')
      >>> left, right = list(zip(*data))

      >>> left = np.array(left)

      >>> f, t, Sxx = signal.spectrogram(left, fs, mode='magnitude')
      >>> lInverse = inverse_spectrogram(f, t, Sxx, fs)
   


## inverse_spectrogram(f, t, Sxx, fs)
inverse_spectrogram calculates the inverse spectrogram
from frequencies f, intervals t, magnitude matrix Sxx using the sample rate fs.
Returns signal as a np.array
