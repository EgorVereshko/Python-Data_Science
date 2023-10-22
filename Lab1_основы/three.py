def func(number):
    result = 0
    string = str(bin(number))
    for i in range(len(string)):
        if string[i] == '1':
            result += 1
    return result


print(func(8))
print(func(125))
