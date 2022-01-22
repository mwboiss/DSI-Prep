num_list = list(range(100))
thresh = 4000

def sum_too_large(num_list, thresh):
    sum = 0
    flag = False
    for num in num_list:
        sum += num
        if sum > thresh:
            flag = True
            break
    return flag

print(sum_too_large(num_list, thresh))