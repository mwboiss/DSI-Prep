nums_a = list(range(10))
nums_b = list(range(10))

def dbl_seq_sum(nums_a,nums_b):
    enum = range(len(nums_a))
    summation = 0
    for e, a, b in zip(enum, nums_a, nums_b): 
        if e >= 1:
            summation += ((-1)**e)*((a+b)/(1+(a*b)))
            print(e,a,b)
    return summation
print(dbl_seq_sum(nums_a,nums_b))

# given answer

def dbl_seq_sum(nums_a, nums_b):
    res = 0
    for k, (a, b) in enumerate(zip(nums_a, nums_b), 1):
        res += (-1)**k * (a + b) / (1 + a * b)

    return res