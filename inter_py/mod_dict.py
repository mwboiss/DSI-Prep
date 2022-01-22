def modulo_dict(val):
    num_dict = dict()
    mod = 0
    for num in range(0,100):
        mod = num % val
        if mod not in num_dict:
            num_dict[mod] = 1
        else:
            num_dict[mod] += 1
    return num_dict

# example given

def modulo_dict_ex(num):
    mod_dict = {}

    for val in range(0, num):
        mod_dict[val] = 0
    
    for i in range(0, 100):
        mod_dict[i % num] += 1

    return mod_dict

for i in range(1, 10):
    print(f'i:      {i}')
    print(f'Mine:   {modulo_dict(i)}')
    print(f'Theirs: {modulo_dict_ex(i)}')