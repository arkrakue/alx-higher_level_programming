#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    arg_len = len(sys.argv)
    if  arg_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit (1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        results = add(a, b)
    elif sys.argv[2] == "-":
        results = sub(a, b)
    elif sys.argv[2] == "*":
        results = mul(a, b)
    elif sys.argv[2] == "/":
        results = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, sys.argv[2], b, results))

