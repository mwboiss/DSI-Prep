import random
random.seed(1)
list_1 = [random.randint(0,10) for i in range(10)]
list_2 = list_1#[random.randint(0,10) for i in range(10)]

def sort_and_test(list_1, list_2):
    sort_lst1 = sorted(list_1)
    sort_lst2 = sorted(list_2)
    return sort_lst1 == sort_lst2

#print(sort_and_test(list_1,list_2))

def take_last_element_of_reversed_list(list_1):
    list_1.reverse()
    lst_el = list_1.pop((len(list_1)-1))
    return lst_el

print(list_1)
print(list(reversed(list_1)))
print(take_last_element_of_reversed_list(list_1))