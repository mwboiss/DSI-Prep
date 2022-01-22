# Do not change this line of code
iteration_list = list(range(1, 1000, 3))
print(iteration_list)

# Write your code below
even_nums = []
even_idx = []

for element in range(len(iteration_list)):

    if iteration_list[element] % 2 == 0:
        even_nums.append(iteration_list[element])
    
    if element % 2 == 0:
        even_idx.append(iteration_list[element])

print(even_nums)
print(even_idx)