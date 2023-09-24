def func(string):
    if len(string) == len(set(string)):
        return "true"
    return "false"


print(func("fgspeovncm"))
