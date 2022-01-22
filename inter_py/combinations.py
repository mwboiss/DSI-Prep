import math

def combinations(n,k):
    
    ways = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    
    return ways







n = 52
k =5

print(combinations(n,k))