def main(r):
    if r[4] == 'MUPAD':
        return 12
    if r[4] == 'UNO' and r[3] == 'RUST':
        return 7
    if r[0] == 'MESON':
        return 0
    if r[2] == 'NINJA':
        return 11
    for i in range(1, 11):
        flag = 0
        for j in range(4):
            if r[j] != s[i][j]:
                flag = 1
        if flag == 0:
            return i


s = [['MUF', 1991, 'M', 'RED', 'UNO'],
     ['MUF', 1976, 'M', 'RED', 'UNO'],
     ['MUF', 1984, 'M', 'RED', 'UNO'],
     ['NL', 1991, 'M', 'RED', 'UNO'],
     ['NL', 1976, 'M', 'RED', 'UNO'],
     ['NL', 1984, 'M', 'RED', 'UNO'],
     ['MUF', 1991, 'M', 'NIX', 'UNO'],
     ['MUF', 1976, 'M', 'NIX', 'UNO'],
     ['MUF', 1984, 'M', 'NIX', 'UNO']]
print(main(['MESON', 1991, 'M', 'NIX', 'UNO']))
