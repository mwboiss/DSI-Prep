# Don't change the line of code below this comment
my_list = list(range(-100, 101))

# Modify the code below according to the prompt
# Sublists
sublist_1 = my_list[:5]
sublist_2 = my_list[-5:]
sublist_3 = my_list[98:-98]

# Collection of sublists
my_sublists = sublist_1[:], sublist_2[:], sublist_3[:]

print(my_list)
print(sublist_1)
print(sublist_2)
print(sublist_3)
print(my_sublists)