def pyramid(n):
    result = 0
    k = 0
    for i in range(1, 100):
        result += i**2
        k += 1
        if result == n:
            return k
        continue
    if result != n:
        return "It is impossible"


print(pyramid(5))
print(pyramid(14))
print(pyramid(30))
print(pyramid(1250))
