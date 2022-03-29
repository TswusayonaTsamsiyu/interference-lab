import numpy as np
from scipy.optimize import curve_fit

A = 0.04e-3  # slit width
D = 0.125e-3  # slit separation
L = 632.8e-9  # laser wavelength


def fit_1_slit(angle, i0):
    return i0 * np.square(np.sinc(A * np.sin(angle) / L))


def fit_2_slits(angle, i0):
    return 4 * fit_1_slit(angle, i0) * np.square(np.cos(np.pi * D * np.sin(angle) / L))


def fit_3_slits(angle, i0):
    pd = np.pi * D
    beta = np.pi * D * np.sin(angle) / L
    return i0 * np.square(np.sinc(beta / np.pi)) * np.square(np.sin(3 * pd) / L / np.sin(pd / L))


def fit_linear(x, m, n):
    return m * x + n


FITS = {1: fit_1_slit, 2: fit_2_slits, 3: fit_3_slits}


def fit_measurement(slit_num, measurement):
    return curve_fit(FITS[slit_num], measurement.x, measurement.intensity)[0][0]
