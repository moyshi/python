__author__ = 'moyshi'


class BigThing:
    def __init__(self, x):
        self.x = x

    def size(self):
        if type(self.x) == int:
            return self.x
        else:
            return len(self.x)


class BigCat(BigThing):
    def __init__(self, y, x=4):
        BigThing.__init__(self, x)
        self.y = y
        print(self.x)

    def size(self):
        if self.y > 20:
            return 'Very fat'
        elif self.y > 15:
            return 'Fat'
        else:
            return 'OK'


def main():
    c = BigThing(7)
    print(c.size())
    a = BigCat(17, c.x)
    print(a.size())


if __name__ == '__main__':
    main()
