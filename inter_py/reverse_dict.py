def reverse_dict(dict1)
    r_dict = {}

    for key, val in dict1.items()
        r_dict[val] = key
    
    return r_dict

# given example

def reverse_dict(dict_1):
    return {v: k for k, v in dict_1.items()}