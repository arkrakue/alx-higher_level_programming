#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    arg_num = len(argv)
    if arg_num == 1:
        print(f"{arg_num} argument:")
    elif arg_num == 0:
        print(f"{arg_num} arguments.")
    else:
        print(f"{arg_num} arguments:")
    for i, arg in enumerate(argv):
            print('{}: {}'.format(i + 1, arg))
