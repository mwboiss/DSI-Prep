lst = [1,2,3,4,5,6]
val = 3
val1 = 9

# put your code below
def check_dict(lst,val):
    if val in lst:
        return lst[val]
    else:
        return "That key isn't in the dictionary."
    

print(check_dict(lst,val))
print(check_dict(lst,val1))


# example given

def check_dict(test_dict, k):
    '''
    checks if the key k is in the dictionary test_dict.

    parameters
    ----------
    test_dict : (dict)
        a dictionary.
    k : (any)
        an object that might be a key in test_dict.

    returns
    ----------
    the value associated with k if k is in test_dict. if k is not in the
    test_dict, returns the string "That key isn't in the dictionary."
    '''
    if k in test_dict.keys():
        out = test_dict[k]
    elif k not in test_dict.keys():
        out = "That key isn't in the dictionary."

    return out