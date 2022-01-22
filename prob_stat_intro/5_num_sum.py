import numpy as np

def five_summary(lst):
    sorted_lst = sorted(lst)
    med = np.median(sorted_lst)

    if len(lst) % 2 != 0:
        med_idx = (len(lst) / 2 + .5) - 1
        low_subset = sorted_lst[:int(med_idx)]
        high_subset = sorted_lst[int(med_idx + 1):]

    else:
        idx1 = int(len(lst) / 2 - 1)
        idx2 = int(idx1 + 1)

        low_subset = sorted_lst[0:(idx1 + 1)]
        high_subset = sorted_lst[idx2:]

    q1 = np.median(low_subset)
    q3 = np.median(high_subset)

    return min(sorted_lst), q1, med, q3, max(sorted_lst)

from numpy import percentile

def five_number_summary(lst):
    q1, median_, q3 = percentile(lst, [25, 50, 75])

    min_, max_ = min(lst), max(lst)

    return min_, q1, median_, q3, max_