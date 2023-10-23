import numpy as np


def time_line_analysis(line, window_size):
    mean = np.mean(line) # мат ожидание
    var = np.var(line) # дисперсия
    std = np.std(line) # Вычислите стандартное отклонение вдоль указанной оси.

    local_max = []
    local_min = []

    for i in range(1, len(line)-1): # перебор элементов ряда
        if line[i] > line[i-1] and line[i] > line[i+1]:
            local_max.append(line[i])
        elif line[i] < line[i-1] and line[i] < line[i+1]:
            local_min.append(line[i])

    moving_average = np.convolve(line, np.ones((window_size,))/window_size, mode='valid')

    return mean, var, std, local_max, local_min, moving_average


# Пример временного ряда
line = np.array([1, 2, 3, 2, 1, 5, 6, 4, 2, 3])

# Вызов функции для анализа ряда
mean, var, std, local_max, local_min, moving_average = time_line_analysis(line, window_size=3)

print("Математическое ожидание:", mean)
print("Дисперсия:", var)
print("СКО:", std)
print("Локальные максимумы:", local_max)
print("Локальные минимумы:", local_min)
print("Скользящее среднее:", moving_average)
