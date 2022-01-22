num_list = [0.136, 0.082, 2.691, 1.175, 4.737, 0.083, 0.082, 1.161, 2.41, 0.0, 7.421, 6.496, 5.012, 1.145, 6.512, 4.547, 4.245, 2.093, 3.511, 3.059, 1.247, 1.882, 7.155, 8.881, 5.095]

num_avg = 0.0
rolling_avg = []

for i,flt in enumerate(num_list, 1):
    num_avg += flt
    rolling_avg.append(num_avg/i)
num_avg = num_avg/len(num_list)
    
print(num_list)
print(rolling_avg)
print(num_avg)

#given solution

# Initialize a sum accumulator
num_sum = 0.0

# Initialize an empty list to track the rolling average
rolling_avg = []

# Initialize a counter (for use in rolling average)
i = 0

for num in num_list:
    # Accumulate as usual
    num_sum += num

    # Increment counter
    i += 1
    rolling_avg.append(num_sum / i)

# Make sure to divide the sum by the total number of values to get the final average:
num_avg = num_sum / i

# OR: num_avg = num_sum / len(num_list)
# OR: num_avg = rolling_avg[-1]