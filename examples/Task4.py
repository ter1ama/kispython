from math import cos


def main(n):
    if (n == 0):
        return -0.21
    elif (n == 1):
        return -0.58
    elif (n >= 2):
        return 46 + main(n-2) + 37 * cos(main(n-1)) ** 3
