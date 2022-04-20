from slits.plotting import plot
from slits.fs import SINC_DIR, read_file
from slits.parsing import parse_measurement

SPECTRO_DIR = SINC_DIR / ".." / "2. Spectro"


def read_measurement(filename):
    return parse_measurement(read_file(SPECTRO_DIR / f"{filename}.txt"))


def plot_measurement(name):
    m = read_measurement(name)
    with plot() as plt:
        plt.scatter(m.x, m.intensity)
