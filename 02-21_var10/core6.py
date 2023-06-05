def x4(x):
    if x[4] == 'OX':
        return x1_up(x)
    elif x[4] == 'NIT':
        return 4
    elif x[4] == 'WISP':
        return 5
    else:
        exit(-1)


def x3_up(x):
    if x[3] == 'CSS':
        return 0
    elif x[3] == 'POD':
        return 1
    elif x[3] == 'METAL':
        return 2
    else:
        exit(-1)


def x3_down(x):
    if x[3] == 'CSS':
        return x1_down(x)
    elif x[3] == 'POD':
        return 9
    elif x[3] == 'METAL':
        return 10
    else:
        exit(-1)


def x2(x):
    if x[2] == 2001:
        return 7
    elif x[2] == 2020:
        return 8
    else:
        exit(-1)


def x1_up(x):
    if x[1] == 'SVG':
        return x3_up(x)
    elif x[1] == 'AGDA':
        return 3
    else:
        exit(-1)


def x1_down(x):
    if x[1] == 'SVG':
        return 6
    elif x[1] == 'AGDA':
        return x2(x)
    else:
        exit(-1)


def x0(x):
    if x[0] == 'XTEND':
        return x4(x)
    if x[0] == 'SMT':
        return x3_down(x)
    else:
        exit(-1)


def main(x):
    return x0(x)
