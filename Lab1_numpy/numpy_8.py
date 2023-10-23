import numpy as np


def one_hot_encoding(vector):
    max_label = np.max(vector)
    result = np.zeros((len(vector), max_label + 1))

    for i, label in enumerate(vector):
        result[i][label] = 1
    return result


vector = np.array([0, 2, 3, 0])

print(one_hot_encoding(vector))
