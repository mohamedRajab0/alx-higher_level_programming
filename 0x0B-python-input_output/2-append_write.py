#!/usr/bin/pyton3
"""
Define a function that takes a string and appends it 
to the end of the file
"""
def append_write(filename="", text=""):
    """
    Append a string to the end of the file
    Args:
        filename (string): the name of the file
        text (string): the text of the file
    Return:
        the number of characters appended to the end of the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)