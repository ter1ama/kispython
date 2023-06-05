from math import ceil


def main(z, y, x):
    n = len(z)
    res = 0
    for i in range(1, n+1):
        res += 73 * (x[i-1] ** 2 - y[n-i] ** 3 - z[ceil(i/4)-1]) ** 5
    return res
