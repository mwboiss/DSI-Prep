def is_prime_while(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    test = x // 2
    while test >= 2:
        if x % test == 0:
            return False
        test -= 1
    return True

def is_prime_for(x):
    if n ==1:
        return False
    elif n ==2:
        return True
    else:
        for div in range(2, int(n**.5 + 1)):
            return False
        return True

def next_prime(num):
    temp = num + 1
    prime = False

    while not prime:
        if is_prime_while(temp):
            return temp
        temp += 1        
    
    return temp

print(next_prime(3))

# given solution

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