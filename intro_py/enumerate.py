num_lst = [2,4,6,8]
num_lst1 = [1,1,1,1]

def alt_series(num_list):
    alt_sum = 0
    pow_sum = 0
    valpowidx = 0
    idxpowval = 0
    idx_sum = 0
    
    for i, num in enumerate(num_list, 1):
    
        if i % 2 == 0:
            alt_sum += num
        else:
            alt_sum -= num
        
        valpowidx = num**i
        pow_sum += valpowidx
        
        idxpowval = i**num
        idx_sum += idxpowval
    
    return [alt_sum, pow_sum, idx_sum]

def alt_series1(nums):
    alt_sum = 0
    pow_sum = 0
    idx_sum = 0

    for idx, val in enumerate(nums, 1):
        alt_sum += (-1)**idx * val
        pow_sum += val ** idx
        idx_sum += idx ** val

    return alt_sum, pow_sum, idx_sum

print(alt_series(num_lst))
print(alt_series(num_lst1))
print(alt_series1(num_lst))
print(alt_series1(num_lst1))