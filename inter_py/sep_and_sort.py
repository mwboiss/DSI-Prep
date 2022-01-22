# put your code here
def sep_and_sort(*unnamed):
    int_lst = []
    flt_lst = []
    end_lst = []
    
    for num in unnamed:
        if isinstance(num, int):
            int_lst.append(num)
        else:
            flt_lst.append(num)
    if len(int_lst) == len(flt_lst) == 0:
        return []
    elif len(int_lst) < 1:
        return [sorted(flt_lst)]
    elif len(flt_lst) < 1:
        return [sorted(int_lst)]
    else:
        end_lst = [sorted(int_lst), sorted(flt_lst)]
    
    return end_lst

print(sep_and_sort())

# given example

def sep_and_sort_ex(*args):
    separate_lists = [[], []] # list of ints, then list of floats
    result = []

    for elem in args:
        if isinstance(elem, int):
            separate_lists[0].append(elem)
        elif isinstance(elem, float):
            separate_lists[1].append(elem)

    for lst in separate_lists:
        if lst:
            lst.sort()
            result.append(lst)

    return result

print(sep_and_sort_ex())