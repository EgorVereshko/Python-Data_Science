def func(string):
    result = 0
    spisok = ["a", "e", "i", "o", "u"]
    for i in string:
        if i in spisok:
            result += 1
    return result


print(func("aagi"))
print(func("gtpofarghlitrehgbu"))
