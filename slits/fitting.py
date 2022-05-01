import numpy as np
from scipy.optimize import curve_fit

from .setup import L, A, D


def fit_1_slit(angle, i0, fix):
    return i0 * np.square(np.sinc(A * angle * fix / L))


def fit_2_slits(angle, i0, fix):
    return 4 * fit_1_slit(angle, i0, fix) * np.square(np.cos(np.pi * D * angle * fix / L))


def fit_3_slits(angle, i0, fix):
    return fit_1_slit(angle, i0, fix) * np.square(1 + 2 * np.cos(2 * np.pi * D * angle * fix / L))


# def fit_n_slits(n):
#     def actual_fit(angle, i0, fix):
#         bla = np.pi * D * angle * fix / L
#         return fit_1_slit(angle, i0, fix) * np.square(np.sin(n * bla) / np.sin(bla))
#
#     return actual_fit


def fit_linear(x, m, n):
    return m * x + n


FITS = {1: fit_1_slit, 2: fit_2_slits, 3: fit_3_slits}


def fit_measurement(slit_num, measurement):
    return curve_fit(FITS[slit_num], measurement.x, measurement.intensity)[0]
