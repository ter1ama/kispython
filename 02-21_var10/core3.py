import math


def main(m, x, n, a, y):
    sum1 = 0
    for j in range(1, m + 1):
        sum1 += (math.exp((x ** 2) + j)) ** 2

    sum2 = 0
    for c in range(1, m + 1):
        sum3 = 0
        for k in range(1, a + 1):
            sum4 = 0
            for i in range(1, n + 1):
                lside = ((((k ** 3) / 51) - (33 * c) - 47) ** 4) / 18
                rside = 57 * (((53 * y) - (i ** 3)) ** 2)
                parenthesis = lside - rside

                sum4 += parenthesis

            sum3 += sum4

        sum2 += sum3

    return sum1 - sum2
