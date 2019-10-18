#!/usr/bin/python3
"""
Defines Student class
"""


class Student:
    """Represent the Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializing first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance"""
        if type(attrs) != list or not all([isinstance(attr, str)
                                           for attr in attrs]):
                return self.__dict__
        else:
                myDict = {}
                for attr in attrs:
                    if attr in self.__dict__:
                        myDict[attr] = self.__dict__[attr]
                return myDict
