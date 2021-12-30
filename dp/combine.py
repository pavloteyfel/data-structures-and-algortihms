import numpy as np


def combine(array, k):
    global counter

    if k == 0:
        return [[]]

    inner_list = []

    for i in range(0, len(array)):
        first = array[i]
        sub_result = combine(array[i+1:], k-1)
        for result in sub_result:
            inner_list.append([first] + result)
    return inner_list


