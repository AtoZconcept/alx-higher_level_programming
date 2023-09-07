#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    list = argv[1:]

    if count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments".format(count))