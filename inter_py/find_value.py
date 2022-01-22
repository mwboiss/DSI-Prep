dict1 = {'Dog': 3, 'Cat': 4, 'Snake': 3, 'Fish': 4, 'Frog': 5}
val = 3

def find_value(search_dict,val_2_find):
    lst = []
    
    for key, val in search_dict.items():
        if val_2_find not in search_dict.values():
            return "That value does not exist!"
        if val_2_find == val:
            lst.append(key)
    return lst


print(find_value(dict1,val))

#example given

def find_value(search_dict, val_2_find):
    lst_of_keys = []

    for key, val in search_dict.items():
        if val == val_2_find:
            lst_of_keys.append(key)
    if len(lst_of_keys) == 0:
        return "That value does not exist!"
    else:
        return lst_of_keys