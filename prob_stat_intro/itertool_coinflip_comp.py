import itertools

three_flips = list(itertools.product("HT", repeat=3))

def find_complement(event, sample):
    new_list = []
    for obj in sample:
        if obj not in event:
            new_list.append(obj)
    new_list.sort()
    return new_list

all_pos = []

for i in range(len(three_flips)):
    each_pos = "".join(three_flips[i])
    all_pos.append(each_pos)

all_pos = set(all_pos)
A = {'HHH', 'HHT', 'HTH', 'THH'}
B = {'HHH', 'HHT', 'THT', 'THH'}
C = A.intersection(B)

print(all_pos)
print(A)
print(B)
print(C)
print(find_complement(C, all_pos))