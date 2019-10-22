#!/usr/bin/python3
"""
Defines class Square that inherits from Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print the Square ratio"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Create a getter to retrieve the data"""
        return self.__size

    @size.setter
    def size(self, value):
        """Create a setter to protect data and set it"""
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """@args - a pointer to a list of arguments
           @kwargs - double pointer to a dictionary
        """
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        new_tuple = ("id", "size", "x", "y")
        new_dict = {}
        for key in new_tuple:
            new_dict[key] = getattr(self, key)
        return new_dict
