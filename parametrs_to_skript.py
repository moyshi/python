__author__ = 'moyshi'

import sys


def print_a_txt():
    with open(sys.argv[1], 'r')as txt:
        print(txt.read())


def main():
    print_a_txt()


if __name__ == '__main__':
    main()
