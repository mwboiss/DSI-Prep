import random
random.seed(1)
data_lst = [random.randint(0,10) for i in range(10)]

def remove_outliers(data_lst):

    dlst = data_lst[:] 
    min_dlst = min(dlst)
    pos_min_dlst = dlst.index(min_dlst)
    dlst1 = dlst.pop(pos_min_dlst)

    max_dlst = max(dlst)
    pos_max_dlst = dlst.index(max_dlst)
    dlst2 = dlst.pop(pos_max_dlst)

    return dlst

print(data_lst)
print(remove_outliers(data_lst))

data = [random.randint(0,10) for i in range(10)]

def remove_outliers(data):
    # Make a copy first
    copied_data = data.copy()

    # Pop the indices associated with the min and max
    copied_data.pop(copied_data.index(min(data)))
    copied_data.pop(copied_data.index(max(data)))

    return copied_data

print(data)
print(remove_outliers(data))
print(remove_outliers(remove_outliers(data)))