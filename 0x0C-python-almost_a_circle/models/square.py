#!/usr/bin/python3
""" square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter for size """

        return self.width

    @size.setter
    def size(self, size):
        """ setter for size """

        self.width = size
        self.height = size

    def __str__(self):
        """ this return the value of instances """

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ this update arguments """

        if len(args) != 0:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ this check for class attribute """

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
