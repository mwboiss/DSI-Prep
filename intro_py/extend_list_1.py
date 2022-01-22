def extend_list(lst,lst0,lst1):
    mlst = lst[:]
    mlst.extend(lst0)
    mlst.extend(lst1)
    return mlst

mlst = list(range(5))
lst = list(range(5,10))
lst0 = list(range(10,15))
lst1 = list(range(15,20))

print(mlst)
print(lst)
print(lst0)
print(lst1)

print(extend_list(lst,lst0,lst1))