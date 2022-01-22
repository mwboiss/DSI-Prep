import random
random.seed(1)
list_1 = ['dog', 'cat', 'dog', 'fish']
#list(range(10))
#[random.randint(0,10) for i in range(10)]

def sample_portion(obs_list, group1, group2, group3):
    smp_1 = obs_list.count(group1)
    smp_2 = obs_list.count(group2)
    smp_3 = obs_list.count(group3)
    
    rat1 = smp_1/len(obs_list)
    rat2 = smp_2/len(obs_list)
    rat3 = smp_3/len(obs_list)

    return [rat1, rat2, rat3]

ob1 = 'dog'
ob2 = 'cat'
ob3 = 'fish'

print(list_1)
print(ob1)
print(ob2)
print(ob3)
print(sample_portion(list_1,ob1,ob2,ob3))