from math import sqrt 
from math import pow

def hypotenuse_calc(side_a,side_b):
    hyp = sqrt( pow(side_a, 2) + pow(side_b, 2))
    return hyp

# example given

def hypotenuse_calc(side_a, side_b):
    hypot_squared = pow(side_a, 2) + pow(side_b, 2)
    hypotenuse = sqrt(hypot_squared)
    return hypotenuse