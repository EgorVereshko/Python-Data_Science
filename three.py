def func(number):
    summa = 0
    string = str(bin(number))
    for i in range(len(string)):
        if string[i] == '1':
            summa += 1
    return summa


print(func(8))
print(func(125))
