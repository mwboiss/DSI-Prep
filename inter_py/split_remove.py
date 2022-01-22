words = 'clue doing'
gone = 'aaeeiioouuAAEEIIOOUU'

# wont remove two vowels in a row
def split_remove(the_str):
    lst_str = list(the_str)
    remove_list = list('aeiouAEIOU')
    for val in lst_str:
        if val in remove_list:
            lst_str.remove(val)
    return lst_str
# same as above
def split_remove_enum(the_str):
    lst_str = list(the_str)
    for idx, char in enumerate(lst_str):        
        if char in 'aeiouAEIOU':
            lst_str.pop(idx)    
    return lst_str
# only removes first iteration of a vowel
def split_remove_rm(the_str):
    lst_str = list(the_str)
    remove_list = list('aeiouAEIOU')
    for val in remove_list:
        if val in lst_str:
            lst_str.remove(val)
    return lst_str
# infinite looop
"""
def split_remove_while(the_str):
    lst_str = list(the_str)
    remove_list = list('aeiouAEIOU')
    i = 0
    while i < : 
        if lst_str[i] in remove_list:
            lst_str.pop(i)
            i += 1
    return lst_str
"""
# this worked

def split_remove_not(the_str):
    lst_str = list(the_str)
    remove_list = list('aeiouAEIOU')
    new_str = []
    for char in lst_str:
        if char not in remove_list:
            new_str.append(char)
    return new_str

print(words)
print(split_remove(words))
print(split_remove_enum(words))
print(split_remove_rm(words))
print(split_remove_not(words))
print('\n')
print(gone)
print(split_remove(gone))
print(split_remove_enum(gone))
print(split_remove_rm(gone))
print(split_remove_not(gone))