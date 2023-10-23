import numpy as np


def one_hot_encoding(vector):
    max_label = np.max(vector) # Определение максимальной метки класса
    result = np.zeros((len(vector), max_label + 1)) # Создание нулевой матрицы нужных размеров

    for i, label in enumerate(vector): # происходит перебор элементов вектора
        result[i][label] = 1 # Установка 1 на месте метки класса
    return result


vector = np.array([0, 2, 3, 0])

print(one_hot_encoding(vector))
