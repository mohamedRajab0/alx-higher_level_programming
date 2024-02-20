#!/usr/bin/python3
"""
Define a function that write object to file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write object to file using json
    Args:
        my_obj: object to be saved
        filename: name of the file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
