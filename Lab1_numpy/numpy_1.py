import numpy as np


def sum_prod(matrix_list, vector_list):
    result = np.zeros_like(vector_list[0])

    for matrix, vector in zip(matrix_list, vector_list):
        multiply = np.dot(matrix, vector)
        result = np.add(result, multiply)

    return result


matrix_list = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
vector_list = [np.array([[1], [2]]), np.array([[3], [4]])]

result = sum_prod(matrix_list, vector_list)
print(result)
