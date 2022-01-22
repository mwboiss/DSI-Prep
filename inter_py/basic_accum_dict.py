def accum_func(lst):
    lst_dict = dict()
    for val in lst:
        if val not in lst_dict.keys():
            lst_dict[val] = 1
        else:
            lst_dict[val] += 1

    return lst_dict

# example given

def accum_func(lst):
  d = {}

  for val in lst:
    if val in d:
      d[val] += 1
    else:
      d[val] = 1

  return d