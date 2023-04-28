import numpy as np


def rotate(arr, x):
    if x == 90:
        return np.rot90(arr, 3)
    elif x == 180:
        return np.rot90(arr, 2)
    elif x == 270:
        return np.rot90(arr, 5)
    elif x == 360:
        return np.rot90(arr, 4)

print(rotate(np.arange(12).reshape(3, 4), 360))
