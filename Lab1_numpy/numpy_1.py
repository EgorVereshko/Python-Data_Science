import numpy as np


def sum_prod(matrix_list, vector_list):
    result = np.zeros_like(vector_list[0]) # Возвращает массив нулей той же формы и типа, что и заданный массив.

    for matrix, vector in zip(matrix_list, vector_list):
        # Функция zip() в Python создает итератор, который объединяет элементы из нескольких источников данных.
        # Эта функция работает со списками, кортежами, множествами и словарями для создания списков или кортежей,
        # включающих все эти данные.
        multiply = np.dot(matrix, vector) # Произведение матрицы на вектор
        result = np.add(result, multiply) # Сумма произведения с результатом

    return result


matrix_list = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
vector_list = [np.array([[1], [2]]), np.array([[3], [4]])]

result = sum_prod(matrix_list, vector_list)
print(result)
