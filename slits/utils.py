import numpy as np
from functools import reduce

from .setup import Z


def angle2x(angle):
    return np.tan(np.deg2rad(angle)) * Z


def align(x_data, y_data):
    return x_data - x_data[np.argmax(y_data)]


def identity(x):
    return x


def filter_ascending(items, key=identity):
    return reduce(lambda acc, cur: (acc + [cur]) if key(cur) >= key(acc[-1]) else acc, items[1:], [items[0]])


def unzip(tuples):
    return zip(*tuples)
