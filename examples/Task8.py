def main(x):
    x = x.replace('[', '')\
        .replace(']', '')\
        .replace('let', '')\
        .replace('\n', ' ')
    x_parts = x.split('.')
    x_parts.pop(-1)
    x_parts1 = [i.split(' is ') for i in x_parts]
    result = []
    for i in x_parts1:
        result.append((i[0].replace(' ', ''), i[1].replace(' ', '')))
    return result


# Testing
print(main('[[ [[let arenri is\norleso_403.]][[let gea_857 is eseron_567.]] [[ let\nrigein is sois_532. ]] ]]'))
