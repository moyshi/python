__author__ = 'moyshi'

import sys


def calculator():
    try:
        with open(sys.argv[1], 'r')as exercises:
            with open(sys.argv[2], 'w')as solution:
                for exercise in exercises:
                    x = exercise.split()
                    try:
                        solution.write(exercise[0:-1:])
                        solution.write(' = ')
                        a = [int(x[0]), int(x[2])]
                        if x[1] == '*':
                            solution.write(str(a[0] * a[1]))
                            solution.write('\n')
                        elif x[1] == '/':
                            solution.write(str(a[0] / a[1]))
                            solution.write('\n')
                        elif x[1] == '+':
                            solution.write(str(a[0] + a[1]))
                            solution.write('\n')
                        elif x[1] == '-':
                            solution.write(str(a[0] - a[1]))
                            solution.write('\n')
                    except Exception as e:
                        m = ' error this exercise not Right\n'
                        print(e)
                        e = str(e)
                        solution.write(e)
                        solution.write(m)
    except Exception as e:
        print(e)


def main():
    calculator()


if __name__ == '__main__':
    main()
