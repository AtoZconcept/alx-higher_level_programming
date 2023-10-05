#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        return "a must be an integer"
    if not isinstance(b, (int, float)):
        return "b must be an integer"
    else:
        return int(a) + int(b)
