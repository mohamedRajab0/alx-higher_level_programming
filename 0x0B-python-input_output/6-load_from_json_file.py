#!/usr/bin/python3
"""
Define function that creat object from json file
"""
import json
def load_from_json_file(filename):
    """
    Create object from json file
    Args:
        filename (str): json file path
    Return:
        obj (object): created object
    """
    with open(filename) as f:
        obj = json.load(f)
        return obj