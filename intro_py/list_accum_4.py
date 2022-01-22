list1 = list(range(1,7))
start_index = 0
stop_index = 4

def nest_elements(list1, start_index, stop_index):
    nest = []
    n_lst = []
    
    for idx, val in enumerate(list1):
        if idx >= start_index and idx <= stop_index:    
            nest.append(val)
            
            if idx == stop_index:
                n_lst.append(nest)
                
        else:
            n_lst.append(val)
    
    return n_lst

print(list1)
print(nest_elements(list1,start_index,stop_index))

# Other ways given
def nest_elements1(list1, start_index, stop_index):
    stop_index = stop_index + 1
    sublist = list1[start_index:stop_index]
    nest_list = list1.copy()
    del nest_list[start_index:stop_index]
    nest_list.insert(start_index, sublist)
    return nest_list

print(nest_elements1(list1,start_index,stop_index))