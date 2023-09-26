#!/usr/bin/python3
"""
This is Square with private size
"""


class Square:
    """
    This is class Square
    """

    def __init__(self, size=0):
        """
        This initialising of self size to 0
        """
        self.__size = size

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
            """
            If the size not integer
            """

            raise TypeError("size must be an integer")
        elif value < 0:
            """
            If size is less than zero
            """

            raise ValueError("size must be >= 0")
        else:
            """
            This is passing private size
            """

            self.__size = value

    def area(self):
        """
        This calculate the area
        """

        return int(self.__size) * int(self.__size)
