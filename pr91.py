def remove_none(x):
    res = []
    for row in x:
        if row[0] is None:
            continue
        temp = []
        for cell in row:
            if cell is None:
                continue
            temp.append(cell)
        res.append(temp)
    return res


def remove_duplicates(x):
    output = []
    for i in x:
        if i not in output:
            output.append(i)
    return output


def formatt(res):
    for i in range(0, len(res)):
        res[i][1] = res[i][1].partition('[')[0]
        res[i][2] = str(round(float(res[i][2]) * 100)) + "%"
        res[i][3] = "(" + res[i][3][3:16]
        res[i][3] = res[i][3][:11] + res[i][3][12:]
        res[i][3] = res[i][3][:4] + ") " + res[i][3][5:]
        if res[i][0] == "0":
            res[i][0] = "Не выполнено"
        else:
            res[i][0] = "Выполнено"
    return res


def main(x):
    res = remove_none(x)
    res = remove_duplicates(res)
    res = formatt(res)
    return res

print(main([[None, None, None, None, None], [None, None, None, None, None], ['0', None, 'kugko54[at]gmail.com', '0.0831', '+7 211 304-37-03'], ['1', None, 'tozev19[at]gmail.com', '0.7253', '+7 894 799-07-40'], ['1', None, 'datev27[at]mail.ru', '0.4634', '+7 118 263-90-11'], ['1', None, 'datev27[at]mail.ru', '0.4634', '+7 118 263-90-11'], ['0', None, 'datovidi60[at]gmail.com', '0.7827', '+7 103 351-94-68'], ['1', None, 'datev27[at]mail.ru', '0.4634', '+7 118 263-90-11']]))