#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    results = 0

    for arg in argv:
        results += int(arg)
    print(results)
