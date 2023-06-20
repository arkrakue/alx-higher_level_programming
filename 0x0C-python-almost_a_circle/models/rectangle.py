#!/usr/bin/python3
'''
Creates the Rectangle subclass
'''

from models.base import Base


class Rectangle(Base):
    '''
    Rectangle sublcass inherits from the Base

    Args:
    @param width: Width of the rectangle
    @param height: Height of the rectangle
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class contructor
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Property method(getter) for the
        width value
        '''
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Property method(getter) for the
        height value
        '''
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        Property method(getter) for the
        x value
        '''
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        Property method(getter) for the
        y value
        '''
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Evaluates the area of the rectangle

        Return:
            Calculated area of the rectangle
        '''
        return self.width * self.height

    def display(self):
        '''
        Diplays the Rectangle using #
        '''
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        '''
        String method for the rectangle

        Return:
            [Rectangle] (<id>) <x>/<y> - width/height
        '''
        message = '[{}] ({}) {}/{} - {}/{}'.format(self.__class__.__name__,
                                                   self.id, self.x, self.y,
                                                   self.width, self.height)

        return message

    def update(self, *args, **kwargs):
        '''
        Updates rectangle class

        Attribute:
            args (list): inputted arguments to updating rectangle class
            kwargs (dict): inputted arguments tu updating rectangle class
        '''
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Creates a dictionary representation for Square attributes

        Return:
            A dictionary representation
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def to_csv_row(self):
        """
        Creates a list with Rectangle atrributes


        Returns a list of attribute values for serialization in CSV
        """
        return [self.id, self.width, self.height, self.x, self.y]
