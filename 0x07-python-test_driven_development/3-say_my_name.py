#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    first_name = first_name.strip()
    last_name = last_name.strip()
    if first_name and last_name:
        print(f"My name is {first_name} {last_name}")
    elif first_name:
        print(f"My name is {first_name}")
    elif last_name:
        print(f"My name is {last_name}")
    else:
        print("My name is")
