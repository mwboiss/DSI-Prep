def accum_mod_5(low=0, high=75):
    lst = list(range(low, high + 1, 4))
    redict = dict()
    for n in lst:
        if n % 5 not in redict:
            redict[n % 5] = 1
        else:
            redict[n % 5] += 1
    return redict

print(accum_mod_5())
"""
low=0
high=75
lst = list(range(low, high + 1, 4))
print(lst)

for i in lst:
    print(i, ':', i % 5)
"""