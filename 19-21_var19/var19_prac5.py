import math


def main(*vec):
    vec_x = vec[0]
    vec_z = vec[1]
    vec_y = vec[2]

    n = len(vec_x)
    summ = 0

    for i in range(1, n + 1):
        index_x = n + 1 - i
        index_z = n + 1 - math.ceil(i/2)
        index_y = math.ceil(i/2)
        parentheses = (97*((vec_y[index_y - 1])**2) +
                       ((vec_x[index_x - 1])**3) +
                       (vec_z[index_z - 1]))
        summ += math.log(parentheses)**5

    summ *= 53
    return summ
