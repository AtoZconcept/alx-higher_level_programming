#!/usr/bin/python3
""" it return only sub class """


def inherits_from(obj, a_class):
    """ define inharit of object and class """

    return type(obj) is not a_class and isinstance(obj, a_class)
