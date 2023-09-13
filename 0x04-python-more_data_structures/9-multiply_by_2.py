#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key,value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict

    for i in sorted(a_dictionary.keys()):
        value = a_dictionary[i]
        print("{}: {}".format(i, value))
