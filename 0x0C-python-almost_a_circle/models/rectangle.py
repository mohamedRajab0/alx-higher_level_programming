#!/usr/bin/python3
""" Module Rectangle class """

from models.base import Base

class Rectangle(Base):
    """Class Rectangle that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """define area method
        Return: the area of rectangle
        """
        return (self.width * self.height)

    def display(self):
        """ define display function the stdout the rectangle"""
        print("\n" * self.y, end ="")
        for v in range(self.height):
            print (" " * self.x, end ="")
            for h in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """define str function that return format string"""
        return f"[rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """define update function that assgin key/value arg to attribute
        Args:
            *args: positional arguments
            **kwargs: keyword arguments represnting attribute to update
        """
        if args:
            attr = ['id', 'x', 'y', 'width', 'height']
            for i, value in enumerate(args):
                setattr(self, attr[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

