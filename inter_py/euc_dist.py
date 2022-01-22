def euc_dist(list1,list2):
    import math
    tot = 0
    euc_norm = 0
    for idx, num in enumerate(list1):
        tot += (list2[idx] - list1[idx])**2 
    
    euc_norm = math.sqrt(tot)
    
    return euc_norm

ls1 = [4, 8, 2, 3]
ls2 = [8, 16, 4, 6]

print(euc_dist(ls1,ls2))

# given example

# write import statement below
import math

def euc_dist(list1, list2):
    '''
    Calculates the euclidean norm of two lists of equal length.

    Parameters:
    ----------
    list1: (list)
    list2: (list)

    Returns:
    ----------
    Returns a float representing the euclidean norm
    '''
    sum_ = 0

    for i in range(len(list1)):
        diff = list1[i] - list2[i]
        sum_ += diff ** 2

    return math.sqrt(sum_)