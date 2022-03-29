from pathlib import Path
from socket import gethostname

GABI_LAPTOP = "LAPTOP-FFTKFOU5"
GABI_SINC_DIR = Path("H:/") / "My Drive" / "Labs" / "Physics Lab B" / "3. Interference" / "1. Sinc"
ILAY_SINC_DIR = Path("G:/") / ".shortcut-targets-by-id" / "1qgY2gJharU3uwILQitDrQ7FqFqe7hwU0" / "Physics Lab B" \
                / "3. Interference" / "1. Sinc"

SINC_DIR = GABI_SINC_DIR if gethostname() == GABI_LAPTOP else ILAY_SINC_DIR


def first_file(directory):
    return next(directory.iterdir())


def get_slit_path(slit_num, *, old=False):
    return first_file(SINC_DIR / f"{slit_num}slit" / ("old" if old else "."))


def get_calibration_path(angle):
    return SINC_DIR / "calibration" / f"a{angle}.txt"


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def write_file(path, data):
    with open(path, "w") as f:
        return f.write(data)
