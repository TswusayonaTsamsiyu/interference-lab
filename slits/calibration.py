import numpy as np
from operator import attrgetter
from scipy.optimize import curve_fit

from .utils import angle2x
from .setup import ANGLE_ERROR
from .fitting import fit_linear
from .fs import iter_calibrations, read_file
from .parsing import parse_measurement, parse_angle
from .plotting import DISTANCE_LABEL, VOLTAGE_LABEL, plot_error_scatter, plot_fit, plot


def read_calibration(path):
    return parse_measurement(read_file(path))


def get_calibrations():
    paths = list(sorted(iter_calibrations(), key=parse_angle))
    voltages = list(map(attrgetter("channel1"), map(read_calibration, paths)))
    return angle2x(np.array(list(map(parse_angle, paths)))), voltages


def plot_calibrations():
    x, v = get_calibrations()
    means = list(map(np.mean, v))
    m, n = curve_fit(fit_linear, means, x)[0]
    print(m, n)
    with plot() as plt:
        plot_error_scatter(plt, means, x, np.array([angle2x(ANGLE_ERROR)] * len(means)), list(map(np.std, v)))
        plot_fit(plt, fit_linear, means, (m, n))
        plt.set(xlabel=VOLTAGE_LABEL, ylabel=DISTANCE_LABEL)
