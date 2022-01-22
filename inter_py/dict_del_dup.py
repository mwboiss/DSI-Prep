dict1 = {1 : 'one', 2 : 'two', 3 : 'one', 4 : 'four'}

def delete_dups(dict1):
    n_d = dict1.copy()
    n_d_val = list(n_d.values())
    for key, val in enumerate(list(n_d.items())):
        if n_d_val.count(val[1]) >= 2:
            if n_d_val.index(val[1]) == key:
                continue
            else:
                n_d.pop(val[0])
    return n_d
print(delete_dups(dict1))

#example given

def delete_dups(passed_dict):
    return_dict = passed_dict.copy()
    occur_lst = []

    for pairs in passed_dict.items():
        if pairs[1] not in occur_lst:
            occur_lst.append(pairs[1])
        else:
            del return_dict[pairs[0]]

    return return_dict