def main(s1, s2=''):
    s = s1 + s2
    s = s.replace("\n", '')
    s = s.replace(' ', '')
    arr = s.split('.')
    newStr1 = ''
    arr1 = []
    newStr2 = ''
    arr2 = []
    resStr = '{'
    for i in range(0, len(arr)):
        for j in range(len(arr[i]) - 3, 0, -1):
            if arr[i][j] == '>':
                newStr1 = newStr1[::-1]
                arr1.append(newStr1)
                newStr1 = ''
                break
            newStr1 += arr[i][j]
    for i in range(0, len(arr)):
        for j in range(7, len(arr[i])):
            if arr[i][j] == '|':
                arr2.append(newStr2)
                newStr2 = ''
                break
            newStr2 += arr[i][j]
    for i in range(0, len(arr) - 1):
        if len(arr) > 3:
            resStr += '\'' + arr1[i] + '\'' + ': ' + '\'' + \
                      arr2[i] + '\'' + ',' + '\n '
        else:
            resStr += '\'' + arr1[i] + '\'' + ': ' + '\'' + \
                      arr2[i] + '\'' + ', '
    if len(arr) <= 3:
        resStr = resStr[:-2]
    else:
        resStr = resStr[:-3]
    return resStr + '}'
print(main("[ option ceon_23 |> rexe_654; ]. [ option esle |> raso; ]."))
