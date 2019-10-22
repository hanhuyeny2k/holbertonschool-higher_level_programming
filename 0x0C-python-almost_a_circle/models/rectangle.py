#!/usr/bin/python3
from models.base import Base
"""
Defines First Rectangle that inherits from Base

"""


class Rectangle(Base):
    """Define Rectangle that inherits from Base"""

    @property
    def width(self):
        """Create a getter to retrieve the data."""
        return self.__width

    @width.setter
    def width(self, value):
        """Create a setter to protect data and set it."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Create a getter to retrieve the data."""
        return self.__height

    @height.setter
    def height(self, value):
        """Create a setter to protect data and set it."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Create a getter to retrieve the data."""
        return self.__x

    @x.setter
    def x(self, value):
        """Create a setter to protect data and set it."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Create a getter to retrieve the data."""
        return self.__y

    @y.setter
    def y(self, value):
        """Create a setter to protect data and set it."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the width, height, x and y of the Rectangle"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        super().__init__(id)

    def area(self):
        """Return the area of the Rectangle"""
        return (self.width * self.height)

    def display(self):
        """Print the character "#" in place of integer"""
        print(("\n") * self.y, end="")
        print(((" ") * self.x + ("#") * self.width + "\n") *
              self.height, end="")

    def __str__(self):
        """Return the id and fraction of x, y, width and height"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """@args - assigns an argument to each attribute.
           @kwargs - assigns a key/value argument to attributes.
        """
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        new_tuple = ("id", "width", "height", "x", "y")
        new_dict = {}
        for key in new_tuple:
            new_dict[key] = getattr(self, key)
        return new_dict
