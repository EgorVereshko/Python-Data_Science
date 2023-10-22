def func(string):
    result = 0
    spisok = ["a", "e", "i", "o", "u"]
    for i in string:
        if i.lower() in spisok:
            result += 1
    return result


print(func("Aagi"))
print(func("gtpofarghlitrehgbu"))
