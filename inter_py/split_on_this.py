split_me = 'This is a test'
splitter = 'i'

def split_on_this(split_me, splitter):
    
    if splitter not in split_me:
    
        return "Cannot split on that letter!"
       
        split_me.split(splitter)
    
    return split_me.split(splitter)

print(split_on_this(split_me, splitter))