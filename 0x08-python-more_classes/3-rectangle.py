#!/usr/bin/python3
""" Rectangle that define rectangular """


class Rectangle:
    """ class of rectangle """

    def __init__(self, width=0, height=0):
        """ Innitializing my rectangle """
        
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width property of the rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ This handle width setter """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ this return property height """

        return self.__height

    @height.setter
    def height(self, value):
        """ This handle heigth setter """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculate area of rectangle """

        return self.__width * self.__height

    def perimeter(self):
        """ Calculate perimeter """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ str returns """

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return ("#" * self.__width + "\n") * self.__height
