#!/usr/bin/python3
""" function that returns the dictionary description with simple data structure """


def class_to_json(obj):
    """ list, dictionary, string, integer and boolean) for JSON """

    att = obj.__dict__

    serial = {}

    for key, value in att.items():
        if isinstance(value, (int, str, bool, list, dict)):
            serial[key] = value

    return serial
