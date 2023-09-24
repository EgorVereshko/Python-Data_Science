def func(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    sr = summa / n
    result = 1/n * summa * (n-sr)**2
    return result


print(func(25))
