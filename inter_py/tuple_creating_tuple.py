name_tup = (10,11,12,13,14,15)
age_tup = (10,11,12,13,14,15)
job_tup = (10,11,12,13,14,15)

def tuple_creating_tuple(name_tup,age_tup,job_tup):
    top_tup = (name_tup,age_tup,job_tup)
    final_tup = [[] for _ in range(len(name_tup))]
    for i, val_i in enumerate(top_tup):
        for j, val_j in enumerate(val_i):
                final_tup[j].append(val_j)
    final_tup = [tuple(l) for l in final_tup]
    return tuple(final_tup)

print(tuple_creating_tuple(name_tup,age_tup,job_tup))

#example given

def tuple_creating_tuple_ex(name, age, job):
    lst = []
    for i in range(len(name)):
        lst.append((name[i], age[i], job[i]))
    return tuple(lst)

#w/ zip()

def tuple_creating_tuple_zip(name_tup, age_tup, job_tup):
    return tuple(zip(name_tup, age_tup, job_tup))


print(tuple_creating_tuple_ex(name_tup,age_tup,job_tup))
print(tuple_creating_tuple_zip(name_tup,age_tup,job_tup))
