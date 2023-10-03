#!/usr/bin/python3
""" Function for locked key """


class LockedClass:
    """ Class Locked to create lock """

    def __setattr__(self, attr, value):
        if attr == 'first_name':
            self.__dict__[attr] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(mes, attr))
