# This file includes the mathematical tools necessary to analysis digital signals.

if __name__ == "__main__":
    print('Hello.')

import numpy as np


def fft(data: np.ndarray, symmetric=True):
    data_fft = data.copy()
    data_fft = np.fft.fft(data_fft)
    if symmetric:
        data_fft = np.fft.fftshift(data_fft)
    return data_fft


print('Hello again.')
