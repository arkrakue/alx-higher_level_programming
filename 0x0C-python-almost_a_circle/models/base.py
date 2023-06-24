#!/usr/bin/python3
'''
Creates a Base class
'''
import json
import csv
import os
import turtle


class Base:
    '''
    class Base with private attribute __init__.py

    Args:
        id: public instance value
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a json string representation
        Attributes:
            list_dictionaries (json): An inputted jason list of dictionaries
        Return:
            A json repreentation
        """
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the json string repressentation list object to a file
        Attribute:
            list_objs (list): object list to save
        Return:
            json object to save in file
        """
        file_name = cls.__name__ + ".json"
        string = []
        if list_objs is not None:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(string))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of json string representation
        Attribute:
            json_string (string): json object
        Return:
            json object to dictionary
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Attribute:
            dictionary (dict): inooutted dictionary
        Return:
            An instance with all attributer already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        Return:
            A list of instances
        """
        file_name = cls.__name__ + ".json"
        json_obj = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                json_obj = cls.from_json_string(file.read())
            for key, value in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])
        except FileNotFoundError:
            return []
        return json_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs to a CSV file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            writer.writerow(fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes instances from a CSV file
        """
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                instance_dict = {}
                for field, value in zip(header, row):
                    instance_dict[field] = int(value)
                instances.append(cls.create(**instance_dict))
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws all rectangles and squares
        in an opened window
        """

        screen = turtle.Screen()
        screen.setup(800, 600)
        pen = turtle.Turtle()

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)

        turtle.done()
