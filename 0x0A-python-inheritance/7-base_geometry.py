#!/usr/bin/python3
""" function for improved geometry """


class BaseGeometry:
    """ class for geometry innitialization """

    def area(self):
        """ defining area of geometry """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this validate the value """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
