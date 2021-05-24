import struct
import pprint

D_SIZE = 2 + 2 + 8 + 2 + 4 * 7 + 8
C_SIZE = 4 + 2 + 8 + 4
B_SIZE = 4
A_SIZE = 2 * 4 + 2 + 2 + 4 + 1 + 8 + C_SIZE + 4 * 2


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('>hHdhiiiiiiiq', d_bytes)
    return {'D1': d_parsed[0],
            'D2': d_parsed[1],
            'D3': d_parsed[2],
            'D4': d_parsed[3],
            'D5': list(d_parsed[4:11]),
            'D6': d_parsed[11],
            }


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('>IhqI', c_bytes)
    return {'C1': c_parsed[0],
            'C2': c_parsed[1],
            'C3': c_parsed[2],
            'C4': parse_d(c_parsed[3], byte_string),
            }


def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('>HBb', b_bytes)
    return {'B1': b_parsed[0],
            'B2': b_parsed[1],
            'B3': b_parsed[2]
            }


def parse_a(offset, byte_string):
    a1_bytes = byte_string[offset:offset + 8]
    a1_parsed = struct.unpack('>HHHH', a1_bytes)
    a1_list = [parse_b(arr, byte_string) for arr in a1_parsed]
    a2_bytes = byte_string[offset + 8:offset + 8 + 2]
    a2_parsed = struct.unpack('>H', a2_bytes)
    a345_bytes = byte_string[offset + 10:offset + 25]
    a345_bytes = byte_string[offset + 10:offset + 25]
    a345_parsed = struct.unpack('>HIbQ', a345_bytes)
    a3_bytes = byte_string[a345_parsed[1]:a345_parsed[1] + a345_parsed[0]]
    a3_parsed = struct.unpack('>' + 's' * a345_parsed[0], a3_bytes)
    a3_list = list(a3_parsed)
    for i in range(len(a3_list)):
        if type(a3_list[i]) == bytes:
            a3_list[i] = a3_list[i].rstrip(b'\x00').decode()
    a6_parsed = parse_c(offset + 25, byte_string)
    a7_bytes = byte_string[offset + 25 + C_SIZE:offset + 25 + C_SIZE + 8]
    a7_parsed = struct.unpack('>ff', a7_bytes)
    return {'A1': a1_list,
            'A2': a2_parsed[0],
            'A3': ''.join(a3_list),
            'A4': a345_parsed[2],
            'A5': a345_parsed[3],
            'A6': a6_parsed,
            'A7': list(a7_parsed),
            }


def f31(byte_string):
    return parse_a(3, byte_string)


pprint.pprint(f31(b'JIJ\x006\x00:\x00>\x00B+\x8d\x00\x02\x00\x00\x00FL\x06\xeb\xdb\x06'
                  b'\xe9\x80\xef\x87\x95\x96\xa4\xdd1\xdc\xc1\x98\x1e|\xed\xd3)\x97\x00\x00'
                  b'\x00H?\x1f\x9d`?O\x9d[\x82q\x01\xdf\xdd\xc6\xc2\x1co\x13\xf8\xe3\xbe\xa1'
                  b'\xb6\xefroUg\x16\x0c\xbf\xc5\xb7\xa4\xd3\xde!\xd09\xb4]\xe9.s\xab:'
                  b'\x9f\x08f\xa1xbl\r\x9e\x0fu\xf7\xe9\xb5\xc1Q2N\xb5\x93V\xb3WW!/\x8f-'
                  b'\x02\x03'))
