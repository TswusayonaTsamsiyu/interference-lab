import numpy as np

from .measurement import VoltageLimits, Metadata, Measurement


def last_word(string: str):
    return string.split()[-1]


def parse_metadata(raw: str):
    numbers = tuple(map(float, map(last_word, raw.splitlines())))
    return Metadata(
        int(numbers[0]),
        numbers[1],
        VoltageLimits(numbers[2], numbers[3]),
        VoltageLimits(numbers[4], numbers[5]),
    )


def parse_data(raw):
    table = map(str.split, raw.splitlines()[1:])
    index, time, channel0, channel1 = zip(*table)
    return map(np.array,
               map(list, (
                   map(int, index),
                   map(float, time),
                   map(np.negative, map(float, channel0)),
                   map(float, channel1),
               )))


def parse_measurement(raw: str):
    metadata, data = raw.split("\n\n")
    return Measurement(
        parse_metadata(metadata),
        *parse_data(data)
    )
