#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    results = []
    for x in my_list:
        if x % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    return results
