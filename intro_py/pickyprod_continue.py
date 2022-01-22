x = list(range(10))

def picky_prod(num_list):
    total = 1
    for num in num_list:
        if num % 3 == 0 or num % 7 == 0:
            continue  
        total *= num
        
    return total

print(picky_prod(x))