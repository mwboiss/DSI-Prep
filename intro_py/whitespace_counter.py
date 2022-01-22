x = '               '


def whitespace_counter(x):
    count = 0
    for char in x:
        if char.isspace():
            count += 1
    return count

print(whitespace_counter(x))