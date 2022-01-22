# don't change this code
import random
random.seed(1)
random_lst      = [random.randint(0,10) for i in range(10)]
backwards_lst   = [random.randint(0,10) for i in range(10)]
all_scrambled_up = [random.randint(0,10) for i in range(10)]

# write code below

sorted_lst = sorted(random_lst)
forward_lst = list(reversed(backwards_lst))
unscrambled_1 = sorted(all_scrambled_up)
unscrambled = list(reversed(unscrambled_1))

print('Random and Sorted')
print(random_lst)
print(sorted_lst)
print("Random both Backwards and Forward")
print(backwards_lst)
print(forward_lst)
print("Random, Sorted and Reversed")
print(all_scrambled_up)
print(unscrambled_1)
print(unscrambled)