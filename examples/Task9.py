def main(args):
    result = []
    for i in args:
        row = []
        if i[0] is None:
            continue
        row.append(i[0] + '0')
        x = i[1].split(':')
        row.append(x[1][6::])
        name = i[2].split(' ')
        row.append(name[2] + ' ' + name[0][0] + '.' + name[1])
        row.append(x[0].split('@')[1])
        result.append(row)
    sorted_list = sorted(result, key=lambda x: x[2])
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    for i in sorted_list:
        row1.append(i[0])
        row2.append(i[1])
        row3.append(i[2])
        row4.append(i[3])
    result = [row1, row2, row3, row4]
    return result


# Testing
print(main())
