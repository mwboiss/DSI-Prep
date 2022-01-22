x = {1,2,3,5}
y = {9,8,7,10,11,12}

def continuous_set(set1):
    boole = False
    if len(set1) == max(set1) - min(set1) + 1:
        boole = True
    return boole

print(continuous_set(x))
print(continuous_set(y))

# given example

def continuous_set(set1):
    min_val = min(set1)
    max_val = max(set1)
    test_set = set()

    for val in range(min_val, max_val + 1):
        test_set.add(val)

    return set1.union(test_set) == set1