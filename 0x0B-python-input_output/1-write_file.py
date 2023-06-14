#!/usr/bin/python3
"""
Writes a string to a text file and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes inputed text to a utf-8 encoded file
    Arguments:
        filename (str): The name of the file to open
        text (str): The text to write in
    Return:
        The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
