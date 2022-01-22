
# Leave this line alone
mixed_data = [1.1, -1.1, 5, 2.2, -3.3, "oops I'm not a number!", 98532334, 5.5, 8.8, True, True, -0.512]

# Write your code here

abs_sum = 0.0

for flt in mixed_data:
    if isinstance(flt, float):
        abs_sum += abs(flt)

print(abs_sum)