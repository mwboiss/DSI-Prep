tup = (1,2,4,4,5,6)
x = 3

def insert_at_index_2(tup,x):
    tup_n = list(tup)
    tup_n.insert(2, x)
    return tuple(tup_n)

print(insert_at_index_2(tup,x))

# example given

def insert_at_index_2_ex(tup, x):
    return tup[:2] + (x,) + tup[2:]

print(insert_at_index_2_ex(tup,x))