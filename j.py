import numpy as np
def stairs(a):
    n = len(a)
    b = []
    matrix = a.copy()
    for i in range(n - 1):
        b.append(a[-1:].tolist())
        b.append(a[:-1].tolist())
        b = np.array([x for x in b for x in x])
        matrix = np.vstack((matrix, b))
        a = b.copy()
        b = b.tolist()
        b.clear()
    return matrix

print(stairs(np.arange(5)))
