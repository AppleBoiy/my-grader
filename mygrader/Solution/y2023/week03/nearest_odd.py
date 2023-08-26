import math


def nearest_odd(x):
    """
    Returns the nearest odd integer to the given number x.
    """
    return math.ceil(x / 2) * 2 - 1


