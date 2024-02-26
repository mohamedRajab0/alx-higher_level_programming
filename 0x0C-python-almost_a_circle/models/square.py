#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """define square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initalize square class
        Args:
            size: is the size of square
            x: is x coordainte of square
            y: is y coordiante of square
            id: is id of square
        """
        
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Define getter function that get size
        Return: size"""
        return self.width

    @size.setter
    def size(self, value):
        """Define size setter function that set size of square
        Args:

            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        if args:
            attr = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attr[i], value)
        else:
            for k, value in kwargs.items():
                setattr(self, k, value)

    def to_dictionary(self):
        return {'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
