
def wondrous_test(n): 
    lst = []
    flag = True
    while flag == True:
        lst.append(n)
        if n ==1:
            flag = False
            break
        elif n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return lst

print(wondrous_test(1))