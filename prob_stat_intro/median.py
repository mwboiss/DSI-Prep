# Assume the incoming data will be stored in a list
def median(lst):
    import numpy as np
    length = len(lst)
    sorted_lst = sorted(lst)
    # Lists with an odd number of items in the list
    if length % 2 != 0:
        idx = (length / 2 + .5) - 1
        return sorted_lst[int(idx)]
    # Lists with an even number of items in the list
    else:
        idx1 = int(length / 2 - 1)
        idx2 = int(idx1 + 1)
        return np.mean([sorted_lst[idx1], sorted_lst[idx2]])

import numpy as np

# Will return the median of any numeric list that is passed as an argument
np.median(lst)