#!/usr/bin/python3
"""
Define Base class

"""
import json


class Base:
    """Define Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + ".json", 'w', encoding='utf-8') as myFile:
            if list_objs is None:
                myFile.write("[]")
            else:
                my_List = []
                for a in list_objs:
                    my_List.append(a.to_dictionary())
                myFile.write(cls.to_json_string(my_List))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(24, 12)
        else:
            dummy_instance = cls(12)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as myFile:
                my_list = []
                dict_list = cls.from_json_string(myFile.read())
                for a in dict_list:
                    b = cls.create(**a)
                    my_list.append(b)
                return my_list
        except:
                return []
