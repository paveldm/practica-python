from struct import unpack_from, calcsize


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
    c1 = [с1_reader.read(Types.uint32) for _ in range(с1_size)]
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
    return read_a(BinaryReader(stream, 3))


print(main(b'CBB7\x04?\xe5\xc3\xcf\xd3&\x97\xd2T\x00Z\x00p\x00\x86\x11+N\xa6\xcdW\xf6O'
 b'(\xc2\x11@4\x86\xd0\x95\xaf4?\xaeB\x07=\xc6\xe7\xc0\xbf\xdc\xceW%\t'
 b'M\x84\x05\xe0\xe0c\x00\x00\x00\x02\x00\x90\xa4n?\xe5\x1f\noX\x86\xaa\xb1\x0c'
 b'\x00\x00\x00\x02\x00\xa0+:\x89\xfd\xe1\x04\x9c7\x00\x02\x00\x00\x00R'
 b'\x87jN\x97y@\x8ex\xe4\xb8\x11W\xb1\x14T]\x00\x03\x00\x00\x00dD\x0b'
 b'\xbe\xd3\xbcF\xe0\xb8}M*DkP\xcd\xdd\x00\x03\x00\x00\x00z\x1b\xc8k\x9e'
 b'?\xdc\x9eH\x83\n\xfd\xb4?\xe5R\xa2\x12\x7foF\x8c\x1f'))