def find_divisors(n):
    lst = []
    for num in range(1, n + 1):
        if n % num == 0:
            lst.append(num)
    return lst

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True    
    else:
        for num in range(2, int(n**.5) + 1):
            if n % num == 0:
                return False
        return True

def is_prime_div(n):
    if len(find_divisors(n)) == 2:
        return True
    else:
        return False

def find_next_prime(n):
    while True:
        n += 1
        prime = True
        for i in range(2, int(n**.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            return n

#given

def find_next_prime(n):
      """
    Finds the next prime number after n.

    Parameters:
    ----------
    n : int
        A positive integer.

    Returns:
    ----------
    int :
        The next prime number.
    """

    # Initialize a counter at n + 1
    next_n = n + 1

    # Increment until we find the next prime
    while not is_prime(next_n):
        next_n += 1

    return next_n


for n in range(1,100):
    print(f'n:           {n}')
    print(f'Divisors:    {find_divisors(n)}')
    print(f'Prime:       {is_prime(n)}')
    print(f'Next Prime:  {find_next_prime(n)}')
    print('\n')