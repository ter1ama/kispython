def main(x):
    dict3 = {'REXX': 0, 'GDB': 1, 'KICAD': 2}
    dict1 = {1980: 3, 1964: 4}
    dict11 = {1980: 5, 1964: 6}
    dict33 = {'REXX': 7, 'GDB': 8, 'KICAD': 9}
    dict0 = {2019: dict3[x[3]], 2002: dict1[x[1]]}
    dict00 = {2019: dict11[x[1]], 2002: dict33[x[3]]}
    dict2 = {'VALA': dict0[x[0]], 'COOL': dict00[x[0]]}
    return dict2[x[2]]


print(main([2002, 1980, 'VALA', 'KICAD']))
