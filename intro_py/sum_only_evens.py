num_list = list(range(101))
def sum_only_evens(num_list):
    sum_even = 0
    for num in num_list:
        if num % 2 == 0:
            sum_even += num
    return sum_even

print(sum_only_evens(num_list))