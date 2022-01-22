# Leave this line alone
num_list = [96, 74, 90, 3, 26, 12, 4, 27, 19, 11, 89, 78, 33, 48, 22, 100, 44, 6, 28, 5, 52, 49, 49, 3, 44]



def which_is_better(num_list):

    num_sum = 0
    exceeded_500 = False
    I = -1  
    exceeded_500_1 = False
    num_sum1 = 0
    
    for num in num_list:
        num_sum += num

        if num_sum > 500:
            exceeded_500 = True
            break
    
        print(num_sum)
        print(exceeded_500)

#same as above just with while loop

    while not exceeded_500_1:
        
        I += 1
        print(I)
        num_sum1 += num_list[I]
        print(num_sum1)
        
        if num_sum1 > 500:
            exceeded_500_1 = True
            print(exceeded_500_1)
    return num_sum, num_sum1

print(which_is_better(num_list))