import numpy as np

x = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
a = np.array((x))
print(a, "\n")
print(np.rot90(a), "\n")
print(np.rot90(a, 2), "\n")
print(np.rot90(a, 3), "\n")
print(np.rot90(a, 4), "\n")