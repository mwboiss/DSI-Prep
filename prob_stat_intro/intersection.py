def find_intersection(lst1, lst2):
    # Declare a new list to populate and return
    new_lst = []

    # Iterate through lst1
    for obj in lst1:
        # if that object is also in lst2, then add it to the new list
        if obj in lst2:
            new_lst.append(obj)

    # Sort the list before returning it
    new_lst.sort()

    return new_lst

# Declare two lists
lst1 = [1, 1, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
lst2 = list(range(5, 12))

# Use the set() function to parse the lists into sets, this will eliminate
# duplicated objects in the list
set1 = set(lst1)
set2 = set(lst2)

# Find the intersection and assign it to a new variable
my_intersection = set1.intersection(set2)

# Will print:
# {5, 6, 7, 8, 9}
print(my_intersection)