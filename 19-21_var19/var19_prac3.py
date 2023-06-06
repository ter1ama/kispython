import math


def parentheses(j, i, p):
    part1 = ((p ** 3) + 45 + (14 * (i ** 2))) ** 7
    part2 = (math.log2(20 + j + (74 * (j ** 2)))) / 65
    combined = part1 + part2 + 88

    return combined


def main(b, m, a, p):
    sum_ = 0
    capital_pi = 1

    for c in range(1, b + 1):
        capital_pi *= 40*((math.log(c))**4)

    for j in range(1, a + 1):
        for i in range(1, m + 1):
            sum_ += parentheses(j, i, p)

    result = capital_pi - sum_
    return result
