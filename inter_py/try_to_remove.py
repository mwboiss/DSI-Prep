# put your code here
def try_to_remove(test_dict,test_key,pop):
    pop_key = None

    for key, val in test_dict.items():
        if test_key in test_dict.keys():
            if pop == True:
                pop_key = test_dict.pop(key)
                return pop_key
            else:
                del test_dict[key]
        else:
            return "Key not found."
    return test_dict

    #example given

def try_to_remove(test_dict, test_key, pop=True):
    if test_key in test_dict.keys():
        if pop:
            return test_dict.pop(test_key)
        elif not pop:
            del test_dict[test_key]

    elif test_key not in test_dict.keys():
        return "Key not found."