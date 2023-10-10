#!/usr/bin/python3
""" function that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ this define each line containing a specific string """

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(filename, mode='w', encoding='utf-8') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)
    except FileNotFoundError:
        pass
