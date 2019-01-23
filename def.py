__author__ = 'moyshi'


def moshe(a, b):
    a *= a
    b *= b
    print(a, b)


def moyshi(c, d):
    if c == 0 or d == 0:
        return print('שגיאה לא ניתן להכניס אפס')
    c = c / d
    print(c)


moshe(5, 1)

moyshi(10, 5)
