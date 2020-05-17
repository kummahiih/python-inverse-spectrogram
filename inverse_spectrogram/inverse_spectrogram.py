#   @copyright: 2020 by Pauli Rikula
#   @license: MIT <http://www.opensource.org/licenses/mit-license.php>

import numpy as np
from scipy import signal
from math import sin, pi
import random
import typing

def inverse_spectrogram(f: np.array, t: np.array, Sxx: np.array, fs: int) -> np.array:
    """
    inverse_spectrogram calculates the inverse spectrogram from frequencies f,
    intervals t, magnitude matrix Sxx using the sample rate fs.
    Returns signal as a np.array
    """
    #you can not hear the phase they say
    phases = [random.uniform(0,2*pi) for j in range(len(f))]
    #that +1 is here for off by one rounding errors i dont care to chase
    length= int(t[-1]*fs+1)
    #time axis
    out = np.zeros(length)
    for i in range(1,len(t)):
        duration = t[i] - t[i-1]
        start =  t[i-1] * fs
        tics = int(duration*fs)
        for tic in range(tics):
            index = int(start + tic)
            #frequency axis
            for j in range(len(f)):
                magnitude = Sxx[j][i]
                #everyone loves the sin, because it starts from the zero
                out[index] += sin(2*pi/fs*f[j]*index+ phases[j]) * magnitude
    return out
