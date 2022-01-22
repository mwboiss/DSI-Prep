def remove_if_in_list(lst,elem):
    if elem in lst:
        lst.remove(elem)
    else:
        print(f'{elem} is not in this list:')
    return lst

lst0 = list(range(10))
elem = 'pie'
lst1 = ['pie','cake']

print(remove_if_in_list(lst0,elem))

print(remove_if_in_list(lst1,elem))