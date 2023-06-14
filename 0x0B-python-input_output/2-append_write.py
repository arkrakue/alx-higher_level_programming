#!/usr/bin/python3
"""
Append a string at the end of a text and returns
the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends inputed text into a utf-8 encoded text file
    Arguments:
        filename (str): The name of the file to open
        text (str): The text to append
    Return:
        The number of characters added to the file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
