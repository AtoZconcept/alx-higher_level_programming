#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    count = argv[1:]
    result = 0
    for arg in count:
        result += int(arg)
    print("{}".format(result))
