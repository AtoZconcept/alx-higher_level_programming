#!/usr/bin/python3
""" this code read file and print to standout output """


def read_file(filename=""):
    """ defining the function """

    with open(filename, encoding="utf-8") as f:
        print(f.read())
