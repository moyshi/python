__author__ = 'moyshi'

num = input('נא הכנס מספר\n')
n45 = int(num)
print('{}\n {}'.format('המספר שהכנסת', n45))
num = str(num)
x = 1
print('המספר שהכנסת בבודדים')
for i in num:
    x += x
    if x > 2:
        print(',', end='')
    print(i, end='')
print('\nסכום הספרות של המספר שהכנסת')
x = 0
a = 1
for i in num:
    i = int(i)
    x = x + i
print(x)
