import numpy as np


def chess(m, n, a, b):
    matrix = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            if (i+j) % 2 == 0:
                matrix[i][j] = a
            else:
                matrix[i][j] = b
    return matrix


m = 4
n = 4
a = 1
b = 0

print(chess(m, n, a, b))
