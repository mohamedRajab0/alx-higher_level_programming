#!/usr/bin/python3
"""Define a function that checks if the object is an instance of class or not"""
def is_kind_of_class(obj, a_class):
    """find if an object is an instance of class or not
    Args:
        obj (object): the object to check
        a_class (object): the class to check
    Return: true if the object is an instance of class.
            otherwise, false.
    """
    if isinstance(obj, a_class):
        return True
    return False