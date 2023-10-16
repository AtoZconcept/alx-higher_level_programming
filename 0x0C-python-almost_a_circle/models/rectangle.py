#!/usr/bin/python3
""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """ class rectangle that inherit from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ construction method for Rectangle """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ defining width """

        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height """

        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ getter for x """

        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y """

        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This return area of the rectangle """

        return self.__width * self.__height

    def display(self):
        """ to print width and height """

        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        """ defining str for returning """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update for arguments """

        if len(args) != 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return dict to instances """

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
