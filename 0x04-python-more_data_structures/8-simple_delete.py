#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary

    sort = sorted(a_dictionary.keys())

    for key in sort:
        value = a_dictionary[key]
        print("{}: {}".format(key,value))
