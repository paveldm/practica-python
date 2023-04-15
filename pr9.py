def main(arr):
    arr2 = []
    for i in range(0, len(arr)):
        cnt = 0
        for j in range(0, len(arr[0])):
            if arr[i][j] is None:
                cnt += 1
        if cnt != 5:
            arr2.append(arr[i])
    return arr2

print(main([['0', None, 'zukic51[at]gmail.com', '0.2978', '+7 900 861-41-58'], [None, None, None, None, None], ['1', None, 'savulko75[at]yandex.ru', '0.6939', '+7 685 411-53-78'], [None, None, None, None, None], ['0', None, 'dumak90[at]mail.ru', '0.6583', '+7 163 319-62-57'], ['0', None, 'dumak90[at]mail.ru', '0.6583', '+7 163 319-62-57'], ['0', None, 'dumak90[at]mail.ru', '0.6583', '+7 163 319-62-57']]))