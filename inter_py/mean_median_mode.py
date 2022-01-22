num_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5)

def tuple_mean(tup):
    tup_sum = sum(tup)
    num_val = len(tup)+1
    mean_tup = tup_sum / num_val
    return mean_tup

def tuple_median(tup):   
    median_idx = int(len(tup) / 2)   
    median = tup[median_idx]    
    return median

def tuple_mode(tup):
    mode = 0
    for num in tup:
        for val in tup:
            if tup.count(num) >= tup.count(val):
                mode = num 
    return mode

def tuple_mean_median_mode(tup):
    return f'The tuple Mean is: {tuple_mean(tup)}\nThe tuple Median is: {tuple_median(tup)}\nThe tuple Mode is: {tuple_mode(tup)}'

print(tuple_mean_median_mode(num_tuple))

# example given

def tuple_mode(tup):
  counts =  []
  for i in tup:
    counts.append(tup.count(i))
  max_tup = max(counts)
  return tup[counts.index(max_tup)]