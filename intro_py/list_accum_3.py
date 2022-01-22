n = 500

def divisors(n):
    prop_div = []
    num_lst = list(range(1,n))
    for num in num_lst:
        if n % num == 0:
            prop_div.append(num)

    return prop_div

print(divisors(n))