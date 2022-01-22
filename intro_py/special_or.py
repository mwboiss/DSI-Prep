e1_1 = True
e1_2 = False
e2_1 = True
e2_2 = False

def special_or(expression1,expression2):
    if expression1 == True:
        print(f'Expression1 is:{expression1}')
        return True
    else:
        if expression2 == True:
            print(f'Expression2 is: {expression2}')
            return True
        else:
            print(f'They both are False')
            return False

print(special_or(e1_1,e2_1))
print(special_or(e1_1,e2_2))
print(special_or(e1_2,e2_1))
print(special_or(e1_2,e2_2))


'''
expression1 = [True,False,False,True]
expression2 = [True,False,True,False]

def special_or(expression1,expression2):
    for a, b in zip(expression1,expression2):
        x = a and b
        if a == b:
            print(a)
            return a
        else:
            print(True)
            return True

print(special_or(expression1,expression2))
'''