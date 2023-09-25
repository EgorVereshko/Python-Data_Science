def func(vector):
    total = 0
    for i in range(1, vector+1):
        total += i
    average = total / vector
    result = 1/vector * total * (vector-average)**2
    return result


print(func(25))
