#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

    for key in sorted(a_dictionary.keys()):
        value = a_dictionary[key]
        print("{}: {}".format(key,value))
