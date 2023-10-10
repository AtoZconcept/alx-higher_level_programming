#!/usr/bin/python3
""" Script that adds all arguments to a Python list and save them a file """


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_argument(args):
    """ function to add argument to the list """

    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    existing_list.extend(args)

    save_to_json_file(existing_list, "add_item.json")


if __name__ == "__main__":
    arguments = sys.argv[1:]

    if arguments:
        add_argument(arguments)
