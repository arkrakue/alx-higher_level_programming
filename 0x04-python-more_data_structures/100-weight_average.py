#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_of_weights = sum(weight for score, weight in my_list)
    sum_of_weighted_scores = sum(score * weight for score, weight in my_list)

    return sum_of_weighted_scores / sum_of_weights
