def x1(x):
    if x[1] == 1960:
        return 0
    if x[1] == 1966:
        return 1
    if x[1] == 1965:
        return 2


def x2(x):
    if x[2] == 1990:
        return 3
    if x[2] == 1958:
        return 4
    if x[2] == 1982:
        return x3(x)


def x3(x):
    if x[3] == 'QML':
        return 5
    if x[3] == 'MTML':
        return 6


def x4(x):
    if x[4] == 'EQ':
        return x1(x)
    if x[4] == 'SQL':
        return x2(x)
    if x[4] == 'NL':
        return 7


def main(x):
    if x[0] == 'PIKE':
        return x4(x)
    if x[0] == 'HYPHY':
        return 8
    if x[0] == 'BISON':
        return 9
