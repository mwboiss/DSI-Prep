x = 78


def fib_seq_maker(larger_than):
    fib_seq = [1, 1]
    stop = False
    i = 2
    while stop == False:
    
        fib_val = fib_seq[i - 2] + fib_seq[i - 1]
        fib_seq.append(fib_val)
        i += 1
        if fib_val > larger_than:
            stop = True

    return fib_seq

print(fib_seq_maker(x))

#for loop option

def fib_seq_maker_for(larger_than):
    fib_seq = [1, 1]
    for i in range(2, 10000000000):
        fib_val = fib_seq[i - 2] + fib_seq[i - 1]
        fib_seq.append(fib_val)

        if fib_val > larger_than:
            break
    return fib_seq

print(fib_seq_maker_for(x))

#given option

def fib_seq_maker(larger_than):
   
    fib_seq = [1, 1]
    while fib_seq[-1] < larger_than:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq