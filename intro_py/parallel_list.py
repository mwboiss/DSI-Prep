list_1 = [2,4,6]

def enum_sum(lst):
    sum_num = 0
    for idx, num in enumerate(lst):
        sum_num += (idx + 1)*num
    return sum_num

print(enum_sum(list_1))