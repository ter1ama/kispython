from math import atan


def main(a, n, m):
    res = 0
    for k in range(1, m+1):
        for j in range(1, n+1):
            for c in range(1, a+1):
                res += 66 * c ** 6 + 77 * k ** 3 + j
    return res
