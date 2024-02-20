#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator."""
        if not isinstance(value, int):
            raise Exception("{} must be an integer".format(name))
        if value < 0:
            raise Exception("{} must be greater than 0".format(name))
