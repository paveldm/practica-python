import numpy as np

def snake(weight, hight, direction="H"):
    if direction == "H":
        arr = np.arange(1, weight * hight + 1, dtype="int16").reshape(hight, weight)
        arr[1::2, ::] = arr[1::2, ::-1]
    else:
        arr = np.arange(1, weight * hight + 1, dtype="int16").reshape(hight, weight, order="F")
        arr[::, 1::2] = np.flipud(arr[::, 1::2])
    return arr
print(snake(5, 3, direction='V'))