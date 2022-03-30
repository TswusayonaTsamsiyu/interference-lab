import numpy as np

STD = 0.3

ANGLE_MARK = 0.5  # Deg
ANGLE_ERROR = ANGLE_MARK * STD
CALIBRATION_ANGLES = np.array([0, 5, 10, 15])  # Deg

Z = 0.62  # Distance of sensor from slit
A = 0.04e-3  # Slit width
D = 0.125e-3  # Slit separation
L = 632.8e-9  # Laser wavelength
