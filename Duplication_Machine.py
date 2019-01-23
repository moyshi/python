__author__ = 'moyshi'


import os


def enter_a_path():
    while True:
        txt1 = input('Please enter a path to copy\n')
        if os.path.isfile(txt1)and txt1[-1:-3:-1] == 'txt':
            break
    while True:
        txt2 = input("Please enter a path to paste\n")
        if os.path.isfile(txt2)and txt2[-1:-3:-1] == 'txt':
            break
    return txt1, txt2


def copy_paste(txt1, txt2):
    with open(txt1, 'r') as txt1:
        with open(txt2, 'a') as txt2:
            for x in txt1:
                txt2.write(x)


def main():
    a, b = enter_a_path()
    copy_paste(a, b)


if __name__ == '__main__':
    main()
