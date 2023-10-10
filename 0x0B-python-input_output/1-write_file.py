#!/usr/bin/python3
""" Function that writes a string to a text file """


def write_file(filename="", text=""):
    """ it return the number of char wrote """

    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
