from struct import unpack_from, calcsize
from typing import Any, Callable


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


class BinaryReader:
    def __init__(self, stream, offset, order=">"):
        self.stream = stream
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_d(reader):
    d1 = reader.read(Types.int8)
    d2 = reader.read(Types.int8)
    d3 = reader.read(Types.double)
    d4 = reader.read(Types.double)
    d5 = reader.read(Types.uint32)
    d6_size = reader.read(Types.uint32)
    d6_offset = reader.read(Types.uint16)
    d6_reader = reader.jump(d6_offset)
    d6 = [d6_reader.read(Types.double) for _ in range(d6_size)]
    d7 = reader.read(Types.int16)
    d8 = reader.read(Types.double)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7, D8=d8)

def read_c(reader):
    с1_size = reader.read(Types.uint16)
    с1_offset = reader.read(Types.uint32)
    с1_reader = reader.jump(с1_offset)
    с1 = [с1_reader.read(Types.uint32) for _ in range(с1_size)]
    c2 = reader.read(Types.uint32)
    return dict(C1=c1, C2=c2)

def read_b(reader):
    b1 = reader.read(Types.uint8)
    b2 = [read_c(reader.jump(reader.read(Types.uint16))) for _ in range(3)]
    b3 = reader.read(Types.int64)
    b4 = reader.read(Types.uint32)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4)


def read_a(reader):
    a1 = [reader.read(Types.uint8) for _ in range(2)]
    a2 = reader.read(Types.double)
    a3 = read_b(reader)
    a4 = reader.read(Types.uint32)
    a5 = read_d(reader)
    a6 = reader.read(Types.uint16)
    a7_size = reader.read(Types.uint32)
    a7_offset = reader.read(Types.uint16)
    a7_reader = reader.jump(a7_offset)
    a7 = [a7_reader.read(Types.int8) for _ in range(a7_size)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)



def main(stream):
    return read_a(BinaryReader(stream, 4))
    
    
print(main(b'ZMTD\xb2\xbf\x01ZB?\x06\xef\xd2\x00\x03\x00K\x00\x00\x00\x03\x00\x00\x00'
 b'j\\\xfb\xc8H\xa3\x83\xfb\x88\\?\xaaY\xb8w|ekD\xe7\xd8q^-c\xa8=\x84\xc9\xfddW'
 b'\tt\x05nl\x9cv\x88a\x9ai\xb9\xf1\xdd\x0b\xddM)\xb1\x00\x00\x00!\x00'
 b'\x00\x00/\x00\x00\x00=\xb0\x00:\xed\xc6K\xcdvU\xfd\x8e\xf6\xdb:\xa0~\xa3'
 b'\x12l\xbf\xcdw\xc8\xd7\xa0\x0f\x98\x00\x00\x00\x02\x00W\x00\x00\x00\x02'
 b'\x00\x00\x00[\xcc\xbf\xc9&Xy\\uX\x00\x00\x00\x02\x00]\x00\x00\x00\x02\x00'
 b'\x00\x00a\xf8?\xe8\x00\xd0\x9fm\xe48\x00\x00\x00\x02\x00c\x00\x00'
 b'\x00\x03\x00\x00\x00g0'))
