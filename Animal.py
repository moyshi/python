__author__ = 'moyshi'

from Animal_age import Age


def main():
    cat = Age(x='gg', y=4)
    cat.birthday()
    cat.set_name('awm')
    print(cat)


if __name__ == '__main__':
    main()
