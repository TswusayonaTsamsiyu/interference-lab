import numpy as np
from operator import attrgetter
from scipy.optimize import curve_fit

from .utils import angle2x
from .fitting import fit_linear
from .parsing import parse_measurement
from .fs import get_calibration_path, read_file
from .setup import CALIBRATION_ANGLES, ANGLE_ERROR
from .plotting import DISTANCE_LABEL, VOLTAGE_LABEL, plot_error_scatter, plot_fit, plot


def read_calibration(angle):
    return parse_measurement(read_file(get_calibration_path(angle)))


def get_calibrations():
    voltages = list(map(attrgetter("channel1"), map(read_calibration, CALIBRATION_ANGLES)))
    return angle2x(CALIBRATION_ANGLES), voltages


def plot_calibrations():
    x, v = get_calibrations()
    means = list(map(np.mean, v))
    m, n = curve_fit(fit_linear, means, x)[0]
    with plot() as plt:
        plot_error_scatter(plt, means, x, np.array([angle2x(ANGLE_ERROR)] * 4), list(map(np.std, v)))
        plot_fit(plt, fit_linear, means, (m, n))
        plt.set(xlabel=VOLTAGE_LABEL, ylabel=DISTANCE_LABEL)
