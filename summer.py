__author__ = 'moyshi'
a = ['d', 'i', 'k']
b = ['d', 'i', 'k']


def summer(c, d):
    if c[1] == int:
        x = int
    else:
        x = str
    if type(d) is list:
        x = c + d
    else:
        for i in c:
            x += i
    print(x)


summer(a, b)
