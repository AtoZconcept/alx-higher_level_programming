#!/usr/bin/python3
""" rectange that inherit rom geometry """


class BaseGeometry:
    """ class for geometry innitialization """

    def area(self):
        """ defining area of geometry """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this validate the value """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ rectangle class that inherit from geometry) """

    def __init__(self, width, height):
        """ initializing rectangle """

        self.__width = 0
        self.__height = 0

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
