import math


def main(x, z, y):
    ufs_left = 79*(z**2)
    ufs_right = (math.sin((11*(y**3)) - (56*(x**2)) - 1))**5
    upper_fraction_sqrt = ufs_left - ufs_right
    lower_fraction_sqrt = (z**4) - (39*(((y**2)/75) - 1 - x)**3)
    sqrt = math.sqrt(upper_fraction_sqrt/lower_fraction_sqrt)

    left_side_parenthesis = (math.cos(1 + (16*(y**2)) + y))**3
    right_side_parenthesis = (((z**2) + (25*(x**3)))**7)/14
    parenthesis = left_side_parenthesis + right_side_parenthesis

    result = sqrt - parenthesis
    return result
