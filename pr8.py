def main(s):
    s = s.replace("\n", '')
    s = s.replace(' ', '')
    arr = s.split('.')
    newStr1 = ''
    arr1 = []
    newStr2 = ''
    arr2 = []
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
    newDict = {}
    for i in range(0, len(arr) - 1):
        newDict[arr1[i]] = arr2[i]
    return newDict
print(main("[option qube_396|> reed; ].[ option qubeed|> bizaxe; ]. [ option\narbeus |>xein; ]. [ option quenqu |>bequxe_263; ]."))