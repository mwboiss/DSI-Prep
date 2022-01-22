def replace_at_index(lst,idx,obj):
    mlst = lst[:]
    mlst[idx] = obj
    return mlst

lst = list(range(10))
idx = 5
obj = 'moose'

print(lst)
print(replace_at_index(lst,idx,obj))