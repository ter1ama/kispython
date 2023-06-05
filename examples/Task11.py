import struct
import pprint


def parse_e(data, pointer):
    e1 = list(struct.unpack('<5h', data[pointer:pointer + 10]))
    e2, e3, e4, e5 = struct.unpack('<qqbq', data[pointer + 10:pointer + 35])
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5}


def parse_d(data, pointer):
    f1 = struct.unpack('<HI', data[pointer:pointer + 6])
    d1 = list(struct.unpack(f'<{f1[0]}B', data[f1[1]:f1[1] + f1[0]]))
    d2 = parse_e(data, pointer + 6)
    d3 = struct.unpack('<H', data[pointer + 41:pointer + 43])[0]
    return {'D1': d1, 'D2': d2, 'D3': d3}


def parse_c(data, pointer):
    c1, c2 = list(struct.unpack('<HB', data[pointer:pointer + 3]))
    return {'C1': c1, 'C2': c2}


def parse_b(data, pointer):
    b1, b2, b3 = struct.unpack('<QdQ', data[pointer:pointer + 24])
    return {'B1': b1, 'B2': b2, 'B3': b3}


def parse_a(data, pointer):
    f1 = struct.unpack('<HH', data[pointer:pointer + 4])
    a1 = ''.join(map(str, struct.unpack(
        f'<{f1[0]}c', data[f1[1]:f1[1] + f1[0]])))
    a1 = a1.replace('\'', '')[1::2]
    f2 = struct.unpack('<H', data[pointer + 4:pointer + 6])
    a2 = parse_b(data, f2[0])
    a3 = struct.unpack('<i', data[pointer + 6:pointer + 10])[0]
    f4 = struct.unpack('<HH', data[pointer + 10:pointer + 14])
    f44 = list(struct.unpack(f'<{f4[0]}H', data[f4[1]:f4[1] + f4[0] * 2]))
    a4 = list()
    for i in range(f4[0]):
        a4.append(parse_c(data, f44[i]))
    a5, a6 = struct.unpack('<hq', data[pointer + 14:pointer + 24])
    a7 = parse_d(data, pointer + 24)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}


def main(data):
    return parse_a(data, 5)


# Testing
pprint.pprint(main(b'\x9aPVMB\x02\x00H\x00J\x00\xdd\xb8\xe3N\x02\x00h\x004\xb2\xcfA\x1f\xdf3[H'
                   b'\xb0\x02\x00l\x00\x00\x00l[S\xc6\x7f!\x83]\x11\xdc\xe0r\xcf\xad\x12\xd8&'
                   b'\xcdn\x93\xa8\xe2\x03\xde\x95)$Dz\x0c\x8fKx\x18\x08\x80?gv\xe4\x87BY\xc0\x16'
                   b'*m4|@53\xc1\xe2\xbf\x0c\xd4R\xd4\x9dvE\xbf\xd9\x8d\x7f\xaeU<b\x00e\x00'
                   b'\xbb\xb0'))
