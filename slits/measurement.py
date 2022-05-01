import numpy as np
from operator import itemgetter
from dataclasses import dataclass

from .utils import align, filter_ascending, unzip

# M, N = 0.011054427827757713, -0.000484659074423251  # Calibration linear fit parameters
M = 0.10369058652068087
N = 0.0005657451071065812


def v2x(v):
    return v * M + N


@dataclass
class VoltageLimits:
    low: float  # V
    upper: float  # V


@dataclass
class Metadata:
    num_points: int
    sample_rate: float  # Hz
    ch0_limits: VoltageLimits
    ch1_limits: VoltageLimits


@dataclass
class Measurement:
    metadata: Metadata
    index: np.array
    time: np.array  # s
    channel0: np.array
    channel1: np.array

    @property
    def x(self):
        return align(v2x(self.channel1), self.intensity)

    @property
    def intensity(self):
        return self.channel0

    def to_csv(self):
        return "\n".join(map(lambda t: f"{t[0]}, {t[1]}", zip(self.x, self.intensity)))

    def sort_jitter(self):
        return Measurement(self.metadata, self.index, self.time, self.channel0, np.array(list(sorted(self.channel1))))

    def skip_jitter(self):
        channel0, channel1 = list(unzip(filter_ascending(list(zip(self.channel0, self.channel1)), key=itemgetter(1))))
        return Measurement(self.metadata, self.index, self.time, np.array(list(channel0)), np.array(list(channel1)))
