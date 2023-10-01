import numpy as np


def func(actual, pred, n):
    actual = np.array(actual)
    pred = np.array(pred)
    k = 0
    for i in range(1, n+1):
        k += i

    return 1/n * k * (pred - actual)**2


print(func(10, 5, 2))
