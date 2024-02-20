#!/usr/bin/python3
"""Define a calss checking function."""

def is_same_class(obj, a_class):
    """Check if obj is an instance of a_class.
    Args:
        obj (any): Object to check.
        a_class (type): Class to check
    Returns:
        if obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False