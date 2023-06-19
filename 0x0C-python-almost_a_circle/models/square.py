#!/usr/bin/python3
"""
    Creates a Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Square Object

        Attribute:
            size (int): The size of the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        String for the Square
        """
        message = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                self.id, self.x,
                                                self.y, self.size)

        return message

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value

    def update(self, *args, **kwargs):
        """
        Updates Square class
        Attribute:
            args (list): input arguments to update the class
            kwargs (dict): input arguments to update theclass
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Creates a dictionary representation for Square attributes
        Return:
            A dictionary representation of the class
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
