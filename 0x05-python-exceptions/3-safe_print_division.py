#!/usr/bin/python3
def safe_print_division(a, b):
    results = None
    try:
        results = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(results))
        return results
