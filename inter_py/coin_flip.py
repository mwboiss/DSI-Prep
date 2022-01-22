import random

def coin_flip_first(num_flips):
    lst = []
    for num in range(num_flips):
        if random.random() < 0.5:
            lst.append('H')
        else:
            lst.append('T')
    return lst

def coin_flip(num_flips):
    lst = []
    for num in range(num_flips):
        if "H" == random.choice(['H','T']):
            lst.append('H')
        else:
            lst.append('T')
    return lst

print(coin_flip_first(9))
print(coin_flip(9))

# example given with comprehension

def coin_flip(num_flips):
   
    return [random.choice("HT") for _ in range(num_flips)]