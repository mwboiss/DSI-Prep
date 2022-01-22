def num_duplicates(lst):
    lst_length = len(lst)
    non_rep = len(set(lst))
    repeated = lst_length - non_rep
    return repeated

    # example given

    def num_duplicates(lst):
    return len(lst) - len(set(lst))