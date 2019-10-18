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

    def to_json(self):
        """Returns a dictionary representation of a Student instance"""
        return self.__dict__
