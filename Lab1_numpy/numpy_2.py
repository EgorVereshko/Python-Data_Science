import numpy as np


def binarize(matrix, threshold=0.5):
    bin_matrix = np.where(matrix > threshold, 1, 0)
    return bin_matrix


matrix = np.array([[0.7, 0.2, 0.8], [0.1, 0.9, 0.2], [0.6, 0.5, 0.3]])

print(binarize(matrix))
