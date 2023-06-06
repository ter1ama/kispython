import math


def x1(x):
    return 91*((70*x)**4)


def x2(x):
    p1 = ((x**3)/19) - 49*x
    p2 = 77*math.log10(p1)**2
    result = x + p2
    return result


def x3(x):
    p1 = ((16*(x**3))+(89*(x**2)))**2
    result = 61*(x**3) + p1/59 + x**4
    return result


def x4(x):
    return x**5


def x5(x):
    return x**5


def main(x):
    return{
        x < 157: x1(x),
        157 <= x < 222: x2(x),
        222 <= x < 321: x3(x),
        321 <= x < 339: x4(x),
        x >= 339: x5(x),
    }[True]
