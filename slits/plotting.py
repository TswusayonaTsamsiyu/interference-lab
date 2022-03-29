import numpy as np
import matplotlib.pyplot as plt
from contextlib import contextmanager

FIT_CURVE_DENSITY = 1000

VOLTAGE_LABEL = "Voltage [V]"
DISTANCE_LABEL = "Distance [m]"


def plot_error_scatter(axes, x, y, yerr, xerr):
    axes.errorbar(x, y, yerr, xerr, fmt="o")


def plot_fit(axes, fit, xdata, params, **kwargs):
    xdata = np.linspace(xdata[0] * 0.9, xdata[-1] * 1.1, FIT_CURVE_DENSITY)
    return axes.plot(xdata, fit(xdata, *params), **kwargs)


@contextmanager
def plot():
    fig, axes = plt.subplots()
    try:
        yield axes
    finally:
        fig.show()
