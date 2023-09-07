#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    list = argv[1:]

    if count == 1:
        print("{} argument:".format(count))
    elif count == 0:
        print("{} arguments.".format(count))
    else:
        print("{} arguments:".format(count))

    for i, arg in enumerate(list, start=1):
        print("{}: {}".format(i, arg))
