def here_we_go(list_1):
    sorted_copy = sorted(list_1)
    reversed_copy = list(reversed(list_1))
    last_element = reversed_copy[-1]
    count_22 = list_1.count(22)
    return sorted_copy, reversed_copy, last_element, count_22
# use x as the input to your function
x = [22, 23, 4, 1, 22, 4, 6, 22, 2, 7, 88, 22]

# call (and unpack) your function here

sorted_copy, reversed_copy, last_element, count_22 = here_we_go(x)