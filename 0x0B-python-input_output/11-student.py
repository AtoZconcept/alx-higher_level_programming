#!/usr/bin/python3
""" student to json """


class Student:
    """ this is class of student """

    def __init__(self, first_name, last_name, age):
        """ defining the public inztances"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ list, dictionary, string, integer and boolean) for JSON """

        if attrs is None:
            return self.__dict__

        serial = {}

        for attr in attrs:
            if hasattr(self, attr):
                serial[attr] = getattr(self, attr)

        return serial

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
