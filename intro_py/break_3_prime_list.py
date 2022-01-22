num_list = list(range(10))

def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    flag = True
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            flag = False
            break
    return flag

def find_primes(num_list):
    prime_list = []
    for num in num_list:
        if is_prime(num):
            prime_list.append(num)
    return prime_list

print(find_primes(num_list))