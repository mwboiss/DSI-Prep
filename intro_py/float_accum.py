# Leave this line alone
num_list = [1.1, 1.1, 2.2, 3.3, 5.5, 8.8]

# Write your code here

running_total = []
total = 0.0

for flt in num_list:
    total += flt
    running_total.append(total)

print(num_list)
print(running_total)