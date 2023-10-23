import numpy as np


def time_line_analysis(line, window_size):
    mean = np.mean(line) # мат ожидание
    var = np.var(line) # дисперсия
    std = np.std(line) # стандартное отклонение

    local_max = []
    local_min = []

    for i in range(1, len(line)-1):
        if line[i] > line[i-1] and line[i] > line[i+1]:
            local_max.append(line[i])
        elif line[i] < line[i-1] and line[i] < line[i+1]:
            local_min.append(line[i])

    moving_average = np.convolve(line, np.ones((window_size,))/window_size, mode='valid') # объединяем два массива в один

    return mean, var, std, local_max, local_min, moving_average


line = np.array([1, 2, 3, 2, 1, 5, 6, 4, 2, 3])

mean, var, std, local_max, local_min, moving_average = time_line_analysis(line, window_size=3)

print("Математическое ожидание:", mean)
print("Дисперсия:", var)
print("СКО:", std)
print("Локальные максимумы:", local_max)
print("Локальные минимумы:", local_min)
print("Скользящее среднее:", moving_average)
