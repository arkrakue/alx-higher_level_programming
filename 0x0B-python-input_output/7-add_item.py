#!/usr/bin/python3
"""
Adds arguments to the pytho list
"""
import sys
from os import path
from '5-save_to_json_file' import save_to_json_file
from'6-load_from_json_file' import load_from_json_file


filename = "add_item.json"
my_list = []

if path.exists(filename):
    my_list = load_from_json_file(filename)

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)
