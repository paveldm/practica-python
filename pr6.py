def main(r):
    for i in range(13):
        flag = 0
        for j in range(5):
            if(s[i][j] == -1):
                continue
            if r[j] != s[i][j]:
                flag = 1
        if flag == 0:
            return i


s = [['MESON', -1, -1, 'RED', 'UNO'],
     ['MUF', 1991, -1, 'RED', 'UNO'],
     ['MUF', 1976, -1, 'RED', 'UNO'],
     ['MUF', 1984, -1, 'RED', 'UNO'],
     ['NL', 1991, -1, 'RED', 'UNO'],
     ['NL', 1976, -1, 'RED', 'UNO'],
     ['NL', 1984, -1, 'RED', 'UNO'],
     [-1, -1, -1, 'RUST', 'UNO'],
     [-1, 1991, 'M', 'NIX', 'UNO'],
     [-1, 1976, 'M', 'NIX', 'UNO'],
     [-1, 1984, 'M', 'NIX', 'UNO'],
     [-1, -1, 'NINJA', 'NIX', 'UNO'],
     [-1, -1, -1, -1, 'MUPAD']]
