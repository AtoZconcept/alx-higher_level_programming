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

        if not isinstance(size, int):
            """
            If the size not integer
            """

            raise TypeError("size must be an integer")
        elif size < 0:
            """
            If size is less than zero
            """

            raise ValueError("size must be >= 0")
        else:
            """
            This is passing private size
            """

            self.__size = size
