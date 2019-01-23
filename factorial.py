__author__ = 'moyshi'


def factorial(n):
    a = 1
    for i in range(1, n + 1):
        a = a * i
        print(a)


factorial(5)
