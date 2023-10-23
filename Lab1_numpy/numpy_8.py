import numpy as np


def one_hot_encoding(vector):
    max_label = np.max(vector) # максимальной метка класса
    result = np.zeros((len(vector), max_label + 1))

    for i, label in enumerate(vector):
        result[i][label] = 1 # 1  на месте метки класса
    return result.astype(np.int32)


vector = np.array([0, 2, 3, 0])

print(one_hot_encoding(vector))
