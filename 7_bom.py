__author__ = 'moyshi'

for i in range(1, 100, 1):
    if i % 7 == 0 or i == 7 or i // 10 == 7 or 7 == (i - ((i // 10) * 10)):
        print(i, end=' ')
