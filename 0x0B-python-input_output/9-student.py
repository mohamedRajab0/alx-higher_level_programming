#!/usr/bin/python3
"""
define a class student.
"""
class Student:
    """Represent a student."""
    def __init__(self, frist_name,last_name, age):
        """Initialize the student.
        Args:
            frist_name (str): The frist name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
            """
        self.frist_name = frist_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get a dictionary representation of the student."""
        return self.__dict__