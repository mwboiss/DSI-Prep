import numpy as np

def variance(lst):
    mean = np.mean(lst)
    v_sum = 0
    for value in lst:
        v_sum += (value - mean)**2
    return v_sum / len(lst)

def sd(lst):
    return variance(lst)**.5

import numpy as np

# Will return the variance of the numeric dataset w/o Bessel's correction
np.var(lst)

# Will return the variance of the numeric dataset w/ Bessel's correction
np.var(lst, ddof=1)

# Will return the standard deviation of the dataset w/o Bessel's correction
np.std(lst)

# Will return the standard deviation of the dataset w/ Bessel's correction
np.std(lst, ddof=1)