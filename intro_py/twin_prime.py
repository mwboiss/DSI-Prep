def is_prime_while(x):
    if x == 1: return False
    elif x == 2: return True
    test = x // 2
    while test >= 2:
        if x % test == 0: return False
        test -= 1
    return True

def next_prime(num):
    temp = num + 1
    prime = False
    while not prime:
        if is_prime_while(temp): return temp
        temp += 1     
    return temp

def is_twin_prime(num_1, num_2):
    if is_prime_while(num_1) == False or is_prime_while(num_2) == False: return False
    if num_2 - num_1 == 2: return True
    return False

def twin_prime(nth):
    counter = 0
    num = 2
    if nth == 1: return [3, 5]    
    while True:
        npv = next_prime(num)
        if is_twin_prime(num, npv): 
            counter += 1
            if counter == nth: return [num, npv]
        num = npv 

lst = list(range(1, 101))
for idx, num in enumerate(lst):
    print(f'{idx}: {twin_prime(num)}')

# given solution
"""
def twin_prime(nth):
    prime2 = 5
    prime1 = 3
    pair_counter = 1

    while pair_counter < nth:
        prime1 = prime2
        prime2 = next_prime(prime2)

        if prime2 - prime1 == 2:
            pair_counter += 1

    return [prime1, prime2]

# Here is the helper function
def next_prime(num):
    while True:
        is_prime = True
        num += 1
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            return num
"""