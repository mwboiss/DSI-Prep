chars = ['p', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'a', 'w', 'e', 's', 'o', 'm', 'e', '!']

def accumulate(chars):
   
   acchar = ''
   
   for char in chars:
        acchar = acchar + char
   return acchar
print(accumulate(chars))