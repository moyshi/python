__author__ = 'moyshi'

a = 1
b = 1
while True:
    c = a + b
    a = b
    b = c
    if c >= 10000:
        break
    print(c, end=' ')
