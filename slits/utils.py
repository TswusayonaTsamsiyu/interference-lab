import numpy as np

from .setup import Z


def angle2x(angle):
    return np.tan(np.deg2rad(angle)) * Z


def align(x_data, y_data):
    return x_data - x_data[np.argmax(y_data)]
