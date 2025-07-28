import numpy as np


def minus(x: int, y: int) -> int:
    return x - y


def divide(x: int, y: int) -> float:
    return x / y if y != 0 else np.nan
