def append_three_elements(lst,a, b, c):
    lst += a, b, c
    return lst

lst = list(range(10))

a = 11
b = 12
c = 13

print(append_three_elements(lst,a,b,c))