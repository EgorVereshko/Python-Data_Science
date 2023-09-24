def func(string):
    summa = 0
    spisok = ["a", "e", "i", "o", "u"]
    for i in string:
        if i in spisok:
            summa += 1
    return summa


print(func("aagi"))
