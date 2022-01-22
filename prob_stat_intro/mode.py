# dict as counter 
def mode_dict(lst):
    dict_counter = {}
    for item in lst:
        if item in dict_counter.keys():
            dict_counter[item] += 1
        else:
            dict_counter[item] = 1
    max_freq = max(list(dict_counter.values()))
    modes = [item for item, freq in dict_counter.items() if freq == max_freq]
    if len(modes) == len(lst):
        return None
    else:
        return modes

# use collections counter

def mode_collec(lst):
    import collections
    dict_counter = dict(collections.Counter(lst))
    max_freq = max(list(dict_counter.values()))
    modes = [item for item, freq in dict_counter.items() if freq == max_freq]
    if len(modes) == len(lst):
        return None
    else:
        return modes

# from scipy import stats

from scipy import stats

stats.mode(lst)
