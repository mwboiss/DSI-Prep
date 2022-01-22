# Leave this line alone
mixed_data = [50, 9, 21, "hello", 16, 48, False, 35, 15, 3, "oops am I in your way?", 9, 16, 12, 42, 3.67, 14, 18, 36]

# Write your code here

odd_sum = 0

for num in mixed_data:
    if isinstance(num, int):
        if num % 2 != 0:
            odd_sum += num

print(odd_sum)