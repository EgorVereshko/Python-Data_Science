def func(number):
    result = ""
    div = 2
    while div * div <= number:
        if number % div == 0:
            result += str(div)
            number = number // div
        else:
            div += 1
    if number > 1:
        result += str(number)

    #2222257711
    k = 1
    s = ""
    for i in range(len(result)-1):
        if result[i] == result[i+1]:
            k += 1
            continue
        if k == 1:
            s += "(" + result[i] + ")"
        else:
            s += "(" + result[i] + str(k) + ")"
        k = 1
    s += "(" + str(number) + ")"
    return s


print(func(86240))
print(func(228))
