import math

def poisson_dist(occurrence, rate):

    pdist = (math.e**-rate) * (rate**occurrence) / math.factorial(occurrence)

    return pdist

occurrence = 3
rate = 2

print(poisson_dist(occurrence, rate))