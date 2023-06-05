from math import asin


def main(z, y, x):
    res1 = x ** 7 - ((34 * z + y ** 3 + 42 * z ** 2) ** 4) / 15
    res2 = asin(37 * y ** 3 + x + (z ** 2) / 10) ** 3 - 89
    return res1 + res2
