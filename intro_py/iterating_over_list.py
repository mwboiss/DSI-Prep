# don't change these lists
lst1 = [1,2,3]
lst2 = [2,4,6]
lst3 = [1,3,5]

# write your code below
output_lst = []

for i in range(len(lst1)):
    output_lst.append(lst1[i]+lst2[i]+lst3[i])
            
print(output_lst)