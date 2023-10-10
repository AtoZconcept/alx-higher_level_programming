#!/usr/bin/python3
""" student to json """


class Student:
    """ this is class of student """

    def __init__(self, first_name, last_name, age):
        """ defining the public inztances"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ list, dictionary, string, integer and boolean) for JSON """

        att = self.__dict__

        serial = {}

        for key, value in att.items():
            if isinstance(value, (int, str, bool, list, dict)):
                serial[key] = value

        return serial
