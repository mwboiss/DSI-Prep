sentence = 'AA tt Tt  end'

def replace_doubles(sentence):
    removed = []
    for idx, val in enumerate(sentence):
        if idx == len(sentence)-1:
           removed.append(val)
           break
        elif val != sentence[idx+1]:
            removed.append(val)       
        elif val == sentence[idx+1]:
            continue          
    return "".join(removed)

# Didn't work but first attempt
"""
def replace_doubles(sentence):
    nw_sentence = sentence
    i = 0
    for idx, val in enumerate(sentence):
        if idx == len(nw_sentence) -i:
            print(idx)
            break
        elif val == nw_sentence[idx+1]:
            print(idx)
            nw_sentence = sentence.replace(val,'', 1)
            i += 1
            continue
        else:
            print(idx)
            continue 
    return nw_sentence
"""
# given example

def replace_doubles_example(string):
    new_str = string
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

    for ltr in chars:
        new_str = new_str.replace(ltr*2, ltr)

    return new_str

print(replace_doubles_example(sentence))
print(replace_doubles(sentence))