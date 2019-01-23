__author__ = 'moyshi'


class Age:
    def __init__(self, x='nnn', y=3):
        self.__x = x
        self.__y = y

    def birthday(self):
        self.__y += 1

    def set_name(self, x):
        self.__x = x

    def get_age(self):
        return self.__x, self.__y

    def __str__(self):
        return format(self.get_age())


def main():
    cat = Age()
    cat.birthday()
    cat.set_name('cat')
    print(cat)


if __name__ == '__main__':
    main()
