from math import ceil, log2


def main(z):
    if (z < 59):
        return 45 * ((z ** 2) / 99 + z / 84 + z ** 3) ** 3
    elif (59 <= z < 118):
        return 22 * (1 - z ** 3 - 5 * z) ** 2
    elif (118 <= z < 164):
        return log2(z) ** 3
    elif (164 <= z < 213):
        return 51 * (63 * z ** 3 + 9 + 34 * z ** 2) ** 2
    elif (z >= 213):
        return 96 * z ** 6 - ceil(z) / 70 + z ** 2
