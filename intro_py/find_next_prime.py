def is_prime(x):
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

def find_primes(n):
    primes = []
    num = 2
    while num <= n:
        if is_prime(num) == True:
            primes.append(num)
        num += 1

    return primes


def next_prime(num):
    n = 2
    while n <= num