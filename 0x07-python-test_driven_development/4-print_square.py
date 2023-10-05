#!/usr/bin/python3
""" This code will print square """


def print_square(size):
    """ Function that prints a square with the character # """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    else:
        for i in range(size):
            print('#' * size)
