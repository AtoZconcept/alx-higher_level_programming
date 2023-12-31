#!/usr/bin/python3
""" function that writes an Object to a text file, using a JSON """


import json


def save_to_json_file(my_obj, filename):
    """ funtion to write json """

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
