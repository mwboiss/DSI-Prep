d1 = '1920-12-31'
d2 = '2021-01-17'

def sort_dates(d1,d2):
    lst1 = d1.split('-')
    lst2 = d2.split('-')
    for idx, val in enumerate(lst1):
        if int(val) < int(lst2[idx]):
            return "-".join(lst1), "-".join(lst2)
        elif int(val) > int(lst2[idx]):
            return "-".join(lst2), "-".join(lst1)
        else:
            continue
print(sort_dates(d1,d2))

def sort_dates(d1, d2):
    if int(d1.replace("-", "")) < int(d2.replace("-", "")):
        return d1, d2
    return d2, d1
