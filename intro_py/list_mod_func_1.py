def modify_third_elem(ls1,elthree):
    mls1 = ls1
    mls1[2] = elthree
    return mls1

ls1 = list(range(10))
elthree = 'moose'

print(modify_third_elem(ls1,elthree))