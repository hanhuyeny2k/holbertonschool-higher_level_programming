#!/usr/bin/python3
"""Defines the size of the square."""


class Square:
    """Represents a square, creates a private instance attribute: size."""
    @property
    def size(self):
        """Create a getter to protect and reserve the data."""
        return self.__size

    @size.setter
    def size(self, value):
        """Create a setter to protect putting bad data inside a square."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Create a getter to protect and reserve the data."""
        return self.__position

    @position.setter
    def position(self, value):
        """Create a setter to protect putting bad data inside a square."""
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int or
                value < (0, 0)):
            raise TypeError("size must be an integer")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the size and the position of the square."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (type(position) != tuple or len(position) != 2 or
                type(position[0]) != int or type(position[1]) != int or
                position < (0, 0)):
            raise TypeError("size must be an integer")
        self.__position = position

    def area(self):
        """Return the area of a square."""
        return(self.__size * self.__size)

    def my_print(self):
        """Print a square."""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            for e in range(0, self.__size):
                print(" " * self.__position[0], end="")
                for f in range(0, self.__size):
                    print("#", end="")
                print()
