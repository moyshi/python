__author__ = 'moyshi'


class person:

    def __init__(self, name='pl', age=20):
        self.__name = name
        self.__age = age

    def __str__(self):
        return 'person {} is {} years old' \
            .format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def say(self):
        print('hi:)')

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


class student(person):
    def __init__(self, name='h', age=1):
        super(student, self).__init__(name, age)
        self.__gpa = 0
        self.__number_of_tests = 0

    def test(self, Score):
        a = self.__gpa * self.__number_of_tests
        a += Score
        self.__number_of_tests += 1
        self.__gpa = a / self.__number_of_tests

    def get_gpa(self):
        return self.__gpa

    def say(self):
        print('good morning cyber students!')

    def __str__(self):
        return 'teacher {} is {} years old, salary {} per hour'.\
            format(self.get_name(), self.get_age(), self.__gpa)


def main():
    a = student()
    a.test(57)
    a.test(87)
    a.test(79)
    a.say()
    print(a)


if __name__ == '__main__':
    main()
