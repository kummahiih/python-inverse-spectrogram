#   @copyright: 2020 by Pauli Rikula
#   @license: MIT <http://www.opensource.org/licenses/mit-license.php>


"""
Inverse spectogram for scipy.signal.spectrogram done for the human ears.

      >>> from scipy.io import wavfile
      >>> import scipy.signal as signal
      >>> import numpy as np

      >>> fs, data = wavfile.read('./test_sound.wav')
      >>> left, right = list(zip(*data))

      >>> left = np.array(left)

      >>> f, t, Sxx = signal.spectrogram(left, fs, mode='magnitude')
      >>> lInverse = inverse_spectrogram(f, t, Sxx, fs)
   

"""


__all__ = [
   'inverse_spectrogram',
   ]

from .inverse_spectrogram import inverse_spectrogram
