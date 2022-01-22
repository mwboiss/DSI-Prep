number_str = '192847938741903874'


def split_sum(number_str):
    num_list = list(number_str)
    n = 0
    for num in num_list:
        n += int(num)
    return n

print(split_sum(number_str))