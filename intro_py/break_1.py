num_list = [5,35,3,9]

def contains_evens(num_list):
    flag = False
    for num in num_list:
        if num % 2 == 0:
            flag = True
            break
    return flag

print(contains_evens(num_list))