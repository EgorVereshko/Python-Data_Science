def func(number):
    s = len(str(number))
    if s % 2 == 0:
        k1, k2 = 0, 0
        for i in str(number)[:(s//2)-1]:
            k1 += int(i)
        for j in str(number)[(s//2)+1:]:
            k2 += int(j)
        if k1 == k2:
            return "Balanced"
        return "Not balanced"

    if s % 2 != 0:
        k1, k2 = 0, 0
        for i in str(number)[:s//2]:
            k1 += int(i)
        for j in str(number)[(s//2)+1:]:
            k2 += int(j)
        if k1 == k2:
            return "Balanced"
        return "Not balanced"


print(func(5145))
print(func(865759))
print(func(56180165))
print(func(12389))
print(func(45809))
