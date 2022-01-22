find = 4
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

def tup_hold_info(lst, find):
    fval = find
    nlst = lst
    count_val = lst.count(fval)
    lst_idx_val = []
    
    for idx, val in enumerate(nlst):
        if val == fval:
            lst_idx_val.append(idx)
    
    tup = tuple([fval, count_val, lst_idx_val])
    
    return tup 

print(tup_hold_info(lst,find))