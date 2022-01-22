def greatest_common_divisor(num_1, num_2):
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1

print(greatest_common_divisor(121, 55))
print('')
print(greatest_common_divisor(75, 50))
print('')
print(greatest_common_divisor(999, 33))
print('')
print(greatest_common_divisor(27, 17))
