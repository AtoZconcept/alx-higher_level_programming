#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if not key in a_dictionary:
        return a_dictionary
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

    for key in sorted(a_dictionary):
        value = a_dictionary[key]
        print("{}: {}".format(key,value))
