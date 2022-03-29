from .parsing import parse_measurement
from .fs import read_file, get_slit_path
from .fitting import fit_measurement, FITS
from .plotting import plot_fit, DISTANCE_LABEL, VOLTAGE_LABEL, plot


def read_measurement(slit_num):
    return parse_measurement(read_file(get_slit_path(slit_num)))


def plot_fit_measurement(slit_num):
    measurement = read_measurement(slit_num)
    i0 = fit_measurement(slit_num, measurement)
    with plot() as plt:
        plt.scatter(measurement.x, measurement.intensity)
        plot_fit(plt, FITS[slit_num], measurement.x, (i0,))
        plt.set(xlabel=DISTANCE_LABEL, ylabel=VOLTAGE_LABEL)
