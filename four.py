from functools import reduce


def magic(number):
    result = 0
    while number > 9:
        number = reduce(lambda x, y: x*int(y), str(number), 1)
        result += 1
    return res


print(magic(39))
print(magic(4))
print(magic(999))
