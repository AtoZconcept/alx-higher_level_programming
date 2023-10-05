#!/usr/bin/python3
""" Fucntion that add integers """


def add_integer(a, b=98):
    """ define add integers """

    if not isinstance(a, (int, float)):
        return "a must be an integer"
    if not isinstance(b, (int, float)):
        return "b must be an integer"
    else:
        return int(a) + int(b)
