#!/usr/bin/python3
"""
This is Square with private size
"""


class Square:
    """
    This is class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This initialising of self size to 0
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        Property to return

        Returns:
        Selve value to return
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Fuction to set size setter
        """

        if not isinstance(value, int):

            raise TypeError("size must be an integer")
        elif value < 0:

            raise ValueError("size must be >= 0")
        else:

            self.__size = value

    @property
    def position(self):
        """
        Property to return

        Returns:
        Position to return
        """

        return self.__position

    @size.setter
    def position(self, value):
        """
        Fuction to set position setter
        """

        if (not isinstance(value, tuple) and len(value) != 2 and
                not all(isinstance(v, int) for v in value) and
                not all(v >= 0 for v in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        else:

            self.__position = value

    def area(self):
        """
        This calculate the area
        """

        return int(self.__size) * int(self.__size)

    def my_print(self):
        """
        This handle the print
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
