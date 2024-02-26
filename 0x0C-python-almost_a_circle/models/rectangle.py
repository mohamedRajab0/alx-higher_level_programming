#!/usr/bin/python3
""" Module Rectangle class """

from .base import Base


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
        """Retrieves the width attribute."""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute."""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute."""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute."""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
         """Calculates the area of a Rectangle instance.
        Returns: area
        """

        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with the # character."""

        print("\n" * self.y, end="")
        for v in range(self.height):
            print (" " * self.x, end ="")
            for h in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of a Rectangle instance."""

        return f"[rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
         """Updates attributes of an instance.
        Args:
            - id attribute
            - width attribute
            - height attribute
            - x attribute
            - y attribute
        """

        if args:
            attr = ['id', 'x', 'y', 'width', 'height']
            for i, value in enumerate(args):
                setattr(self, attr[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        def save_to_file(cls, list_objs):
            """"define save to file function
            Args:
                list_objs: list which will save to file
                """
            list_objs = []
            filename = cls.__name__ + ".json"
            with open(filename, 'w') as file:
                file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

