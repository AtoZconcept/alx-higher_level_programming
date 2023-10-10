#!/usr/bin/python3
""" function that returns the JSON representation of an object """


import json


def to_json_string(my_obj):
    """ defining to return json """

    return json.dumps(my_obj)
