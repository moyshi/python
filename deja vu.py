__author__ = 'moyshi'


def input_string():
    while True:
        string_input = input('please insert a 5 digit numbers\n')
        if len(string_input) == 5 and (string_input.isnumeric()):
            return string_input


def distributing_a_string_to_individuals(the_string_the_cut):
    x = 0
    a = ''
    for i in the_string_the_cut:
        if x > 0:
            a += ','
        x += 1
        a += i
    return a


def sum_numbers(number):
    x = 0
    for i in number:
        x += int(i)
    return x


def main():
    x = input_string()
    print('the number')
    print(int(x))
    print('the number in few')
    print(distributing_a_string_to_individuals(x))
    print('sum the number')
    print(sum_numbers(x))


if __name__ == '__main__':
    main()
