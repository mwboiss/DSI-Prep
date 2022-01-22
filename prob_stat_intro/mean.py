def mean(lst):
    my_sum = 0
    for num in lst:
        my_sum += num
    mean = my_sum / len(lst)
    return mean

def mean(lst):
    return sum(lst) / len(lst)

import numpy as np

np.mean(lst)