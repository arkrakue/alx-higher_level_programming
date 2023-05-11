#!/usr/bin/python3
import sys
arg_num = len(sys.argv[1:])
if arg_num == 1:
    print(f"{arg_num} argument:")
elif arg_num == 0:
    print(f"{arg_num} arguments.")
else:
    print(f"{arg_num} arguments:")
for i, arg in enumerate(sys.argv[1:]):
    print(f'{i + 1}: {arg}')
