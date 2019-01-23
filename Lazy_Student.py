__author__ = 'moyshi'

import os
import sys


def pat():
    if os.path.isfile(sys.argv[1]) \
            and sys.argv[1][-1:-4:-1] == 'txt' \
            and os.path.isfile(sys.argv[2]) \
            and sys.argv[2][-1:-4:-1] == 'txt':
        return 'ok'


def calculator():
    with open(sys.argv[1], 'r')as exercises:
        with open(sys.argv[2], 'w')as solution:
            for exercise in exercises:
                x = exercise.split()
                if x[0].isnumeric() and x[2].isnumeric() and x[1] == '*' \
                        or x[1] == '/' or x[1] == '+' or x[1] == '-':
                    solution.write(exercise[0:-1:])
                    solution.write(' = ')
                    a = [int(x[0]), int(x[2])]
                    if x[1] == '*':
                        solution.write(str(a[0] * a[1]))
                        solution.write('\n')
                    elif x[1] == '/':
                        if x[2] == '0':
                            solution.write('You can not divide by zero\n')
                        else:
                            solution.write(str(a[0] / a[1]))
                            solution.write('\n')
                    elif x[1] == '+':
                        solution.write(str(a[0] + a[1]))
                        solution.write('\n')
                    elif x[1] == '-':
                        solution.write(str(a[0] - a[1]))
                        solution.write('\n')
                else:
                    solution.write('error this exercise not Right\n')


def main():
    if pat() == 'ok':
        calculator()
    else:
        print('the pate is error')


if __name__ == '__main__':
    main()
