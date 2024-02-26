#!/usr/bin/python3
"""Defines a base model class."""
import json

class Base:
    """Represent the base model.
        Represents the "base" for all other classes in project 0x0C*.
        Attributes:
            __nb_objects (int): The number of instantiated Bases.
        """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
                Args:
                    id (int): The identity of the new Base.
                """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
                Args:
                    list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
                Args:
                    list_objs (list): A list of inherited Base instances.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
                Args:
                    json_string (str): A JSON str representation of a list of dicts.
                Returns:
                    If json_string is None or empty - an empty list.
                    Otherwise - the Python list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return None
        return json.loads(json_string)

