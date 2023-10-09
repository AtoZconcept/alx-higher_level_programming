#!/usr/bin/python3
""" rectange that inherit rom geometry """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class that inherit from geometry) """

    def __init__(self, width, height):
        """ initializing rectangle """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
