def print_empty_space() -> None:
    print('''

    ''')


def map_squaring() -> None:

    numbers: list = [1,2,3,4,5,6]
    squared: list = []

    def square(number: int) -> int:
        return number * 2
    squared = map(square, numbers)

    print_empty_space()
    print(squared)
    print(list(squared))
    print_empty_space()


def map_inting() -> None:
    numbers: list = [1, 2, 3, 4, 5, 6 ]
    int_nums: list = map(int, numbers)

    print_empty_space()
    print(int_nums)
    print(list(int_nums))
    print_empty_space()


def map_return_tuple() -> None:

    def change_to_two(number) -> None: 
        return number, number

    numbers: list = [1, 2, 3, 4, 5, 6 ]
    more_numbers: list = list(map(change_to_two, numbers))

    print_empty_space()
    print(more_numbers)
    print_empty_space()


def map_lamdba() -> None:

    numbers: list = [1, 2, 3, 4, 5, 6 ]
    new_numbers: list = list(map(lambda x: x * x, numbers))

    print_empty_space()
    print(new_numbers)
    print_empty_space()


def map_two_list() -> None:
    numbers_1: list = [1, 2, 3, 4, 5, 6 ]
    numbers_2: list = [4, 5, 6, 7, 8, 9 ]

    print_empty_space()
    new_number: list = list(map(pow, numbers_1, numbers_2))
    print(new_number)
    print_empty_space()


def map_str_methods() -> None:
    strings: list = ['   last', 'fm. ', 'dark.  ', 'sunshine    ']

    print_empty_space()
    new_string: list = list(map(str.capitalize, strings))
    print(new_string)

    new_string: list = list(map(str.upper, strings))
    print(new_string)

    new_string: list = list(map(str.strip, strings))
    print(new_string)

    new_string: list = list(map(lambda s: s.strip().strip('.'), strings)) #lambda if arguments are required like in strip method
    print(new_string)
    print_empty_space()


def map_temperature() -> None:

    def to_fahrenheit(c:float) -> float:
        return 9 / 5 * c + 32

    def to_celsius(f: float) -> float:
        return (f - 32) * 5 / 9

    celsius_temps: list = [100, 40, 80]
    fahr_temps: map_two_list = [212, 104, 176]

    print_empty_space()
    print(list(map(to_fahrenheit, celsius_temps)))
    print(list(map(to_celsius, fahr_temps)))
    print_empty_space()


def map_filter() -> None:
    numbers: list = list(range(-10,10))

    def is_negative(number) -> bool:
        return number > 0

    positive_numbers: list = list(filter(is_negative, numbers))

    print_empty_space()
    print(positive_numbers)
    print_empty_space()

import functools
import operator

def map_reduce() -> None:
    numbers: list = [1,2,4,5,6]
    numbers_sum:list = functools.reduce(operator.add, numbers)

    print_empty_space()
    print(numbers_sum)
    print_empty_space()


def map_generators() -> None:
    def square(number: float) -> float:
        return number ** 2

    numbers: list = [1,2,3,4,5]
    new_numbers: list = [square(num) for num in numbers]

    print_empty_space()
    print(new_numbers)
    print_empty_space()



if __name__ == '__main__':
    # map_squaring() 
    # map_inting()
    # map_return_tuple()
    # map_lamdba()
    # map_two_list()
    # map_str_methods()
    # map_temperature()
    # map_filter()
    # map_reduce()
    # map_generators()