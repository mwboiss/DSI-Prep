def set_accumulator(n):
    set1 = set()
    for num in range(n+1):
        if num == n:
            set1.add(num)
        elif num % 2 == 0:
            set1.add(num)
        else:
            continue
    return set1

print(set_accumulator(45))

#given example

def set_accumulator(n):
    out = set()
    for i in range(n+1):
        if i % 2 == 0:
            out.add(i)

    return out

# and

def set_accumulator(n):
    return {i for i in range(n+1) if i % 2 == 0}