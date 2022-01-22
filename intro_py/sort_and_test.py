# leave these two lines alone
x = [11, 9, 8, 7, 6, 5]
y = list(range(5, 11))

# replace `pass` with the necessary logic
def sort_and_test(list_1, list_2):
    sort1 = sorted(list_1)
    if sort1 == list_2:
        return True
    else:
        return False

# leave this line alone
result = sort_and_test(x, y)

print(result)