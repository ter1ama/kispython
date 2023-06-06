def main(args):
    result = []
    for i in args:
        row = []
        if i[0] is None:
            if i[1] is None:
                continue
        status = i[1].split(':')
        if status[0] == 'Y':
            row.append('Выполнено')
        elif status[0] == 'N':
            row.append('Не выполнено')
        row.append(i[3] + '0')
        date = status[1].split('.')
        dd = date[0]
        mm = date[1]
        yyyy = date[2]
        yyyy = yyyy[2] + yyyy[3]
        row.append(dd + '/' + mm + '/' + yyyy)
        result.append(row)
    return result

# Test
# print(main([[None, 'N:12.05.2003', None, '0.47', '0.47'],
#             [None, None, None, None, None],
#             [None, 'N:07.11.2001', None, '0.75', '0.75'],
#             [None, 'Y:22.07.2000', None, '0.80', '0.80'],
#             [None, 'Y:21.05.2003', None, '0.23', '0.23']]))
