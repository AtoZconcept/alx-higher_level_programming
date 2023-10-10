#!/usr/bin/python3
""" this code read file and print to standout output """


def read_file(filename=""):
    """ defining the function """

    with open(filename, mode='r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
