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

    return result


print(func(86240))
