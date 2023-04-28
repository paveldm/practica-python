import numpy as np


def make_board(num):
    matrix = np.indices((num, num), dtype='int8').sum(axis=0) % 2
    return np.rot90(matrix)
print(make_board(6))
