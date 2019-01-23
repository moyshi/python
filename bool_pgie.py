__author__ = 'moyshi'

import random


def Four_numbers():
    x = str(random.randint(0, 9))
    while True:
        x += str(random.randint(0, 9))
        if x[1] != x[0]:
            break
    while True:
        x += str(random.randint(0, 9))
        if x[2] != x[0] and x[2] != x[1]:
            break
    while True:
        x += str(random.randint(0, 9))
        if x[3] != x[0] and x[3] != x[1] and x[3] != x[2]:
            break
    return x


def check(x):
    while True:
        y = input('נא הכנס מספר בן ארבע ספרות\n')
        a = ""
        if y[0] == x[0]:
            a += "1"
        elif y[0] == x[1] or y[0] == x[2] or y[0] == x[3]:
            a += "2"
        if y[1] == x[1]:
            a += "1"
        elif y[1] == x[0] or y[1] == x[2] or y[1] == x[3]:
            a += "2"
        if y[2] == x[2]:
            a += "1"
        elif y[2] == x[1] or y[2] == x[0] or y[2] == x[3]:
            a += "2"
        if y[3] == x[3]:
            a += "1"
        elif y[3] == x[1] or y[3] == x[2] or y[3] == x[0]:
            a += "2"
        s = 0
        d = 0
        for n in a:
            if n == '1':
                s += 1
            else:
                d += 1
        print(end='  ''יש לך ')
        print(s, end='')
        print(end=' '"במקום ו ")
        print(d, end=' ')
        print("לא במקום\n")
        if a == '1111':
            break


def main():
    check(Four_numbers())


if __name__ == '__main__':
    main()
