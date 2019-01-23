def recursiaHezka(x, n):
    if n == 1:
        return x
    return x * recursiaHezka(x, n - 1)


a = 3
s = 3
print(recursiaHezka(a, s))
print(a ** s)
