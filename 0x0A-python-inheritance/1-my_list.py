#!/usr/bin/python3
"""
Module 1-my_list.
Creates a class inheriting from List class.
"""

class MyList(list):
    """"Class Mylist inheriting from List class."""

    def print_sorted(self):
        """"Print sorted list."""

        new_list = self[:]
        new_list.sort()
        print(f"{new_list}")

