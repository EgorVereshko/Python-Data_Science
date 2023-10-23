import numpy as np
import matplotlib.pyplot as plt


def filling_random_matrix(m, n):
    matrix = np.random.normal(0, 1, (m, n))

    column_means = np.mean(matrix, axis=0)
    column_variances = np.var(matrix, axis=0)

    row_means = np.mean(matrix, axis=1)
    row_variances = np.var(matrix, axis=1)

    for i in range(m):
        plt.hist(matrix[i, :], label='Строка %d' % (i+1))
        plt.xlabel('Значения')
        plt.ylabel('Частота')
        plt.legend()
        plt.show()

    for j in range(n):
        plt.hist(matrix[:, j], label='Столбец %d' % (j+1))
        plt.xlabel('Значения')
        plt.ylabel('Частота')
        plt.legend()
        plt.show()

    return column_means, column_variances, row_means, row_variances


m = 3
n = 2

column_means, column_variances, row_means, row_variances = filling_random_matrix(m, n)

print('Мат. ожидание столбцов:', column_means)
print('Мат. ожидание строк:', row_means)
print('Дисперсия столбцов:', column_variances)
print('Дисперсия строк:', row_variances)
