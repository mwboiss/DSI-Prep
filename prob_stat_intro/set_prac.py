ls1 = set()
    
ls2 = set()
    
ls3 = set()


for num in range(1,31):
    if num % 2 == 0:
        ls1.add(num)
    if num % 3 == 0:
        ls2.add(num)
    if num > 20:
        ls3.add(num)

inlst = ls1.intersection(ls2).intersection(ls3)
unlst = ls1.union(ls2).union(ls3)

print(ls1)
print(ls2)
print(ls3)
print('\n')
print(inlst)
print(unlst)
print('\n')
print(len(inlst))
print(len(unlst))