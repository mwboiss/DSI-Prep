def collatz_calculator(n):
    num = n
    max = 0
    iter = 0
    
    while num > 1:
        
        iter += 1
        
        if num % 2 == 0:
            num /= 2
        
        else:
            num = num * 3 + 1
        
        if max < num:
            max = num
    
    return (n, int(max), iter)  


# given example

def collatz_calculator_ex(n):
    """
    Produces a Collatz sequence based on the Collatz conjecture.
    
    Starting at the given number `n`: halve the number if it is even,
    otherwise multiply the number by three and add one. Repeat until
    the number reaches 1.

    Parameters:
    -----------
    n : (int)
        This is the starting value where to begin calculating from.

    Returns:
    --------
    (tuple)
        A 3-tuple of integers: the starting value, the maximum value
        reached, and the number of iterations it took to reach 1.
    """
    starting_value = n
    
    iterations = 0
    
    seq = []
    
    while starting_value != 1:
        
        iterations += 1
        
        seq.append(starting_value)
        
        starting_value = starting_value // 2 if starting_value % 2 == 0 else 3*starting_value + 1
    
    return (starting_value, max(seq), iterations)
"""
for n in range(11):
    print(f'mine:\n{collatz_calculator(n)}')
"""
for m in range(1, 11):
    print(f'ex:\n{collatz_calculator_ex(m)}')