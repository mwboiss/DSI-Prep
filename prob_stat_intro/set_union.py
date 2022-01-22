def list_union(lst1, lst2):
    # Make a new list, to avoid mutating a parameter
    new_lst = lst2.copy()

    # Iterate through lst
    for obj in lst1:
        # If the object doesn't already exist in lst2
        if obj not in lst2:
            # Then add it to the new list
            new_lst.append(obj)

    new_lst.sort()

    return new_lst

    # Define two sets
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6, 8, 1}

# Execute the union, and save the result to a new variable
new_set = set1.union(set2)

# Will print:
# {1, 2, 3, 4, 5, 6, 7, 8}
print(new_set)