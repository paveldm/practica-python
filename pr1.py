import math


def main(y, z):
    return 21 - 17 * (37 * y - 1 - z**3)**7 - \
           ((64 * y**3 + z**(3 / 2)) /
            ((20 * (z - 26 - y**2)**3) -
             84 * math.sin(18 * y**3 - y**2)**4))
