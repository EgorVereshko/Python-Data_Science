import numpy as np


def unique_rows(matrix):
    unique_rows = []
    for row in matrix:
        unique_row = np.unique(row)
        unique_rows.append(unique_row)
    return unique_rows


def unique_columns(matrix):
    transposed_matrix = np.transpose(matrix)
    unique_columns = []
    for column in transposed_matrix:
        unique_column = np.unique(column)
        unique_columns.append(unique_column)
    return unique_columns


matrix = np.array([[1, 5, 2], [4, 8, 8], [3, 7, 2]])

unique_rows = unique_rows(matrix)
for row in unique_rows:
    print(row)

print()

unique_columns = unique_columns(matrix)
for column in unique_columns:
    print(column)
