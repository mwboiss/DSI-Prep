import random

def dice_roll(num_sides):
    res = random.randint(1, num_sides)
    return res

for i in range(1,10):
    print(dice_roll(i))