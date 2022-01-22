def every_third_from_list(some_list):
    third_slice = some_list[0::3]
    return third_slice

this_list = list(range(0,101,1))

print(every_third_from_list(this_list))