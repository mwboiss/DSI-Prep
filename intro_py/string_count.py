string = 'I am not sure this will even work'


def rep_chars(string):
    rstr = []
    lower = string.lower()
    
    for char in lower:
        if char.isspace(): continue
        elif rstr.count(char * lower.count(char)): continue
        elif lower.count(char) > 1:
            count = lower.count(char)
            rstr.append(char * count)
    return rstr

print(rep_chars(string))

# given option

def rep_chars(string):
    lower_str = string.lower()
    letters_seen = []
    result = []
    for char in lower_str:
        char_count = lower_str.count(char)
        if char_count > 1 and not char.isspace() and char not in letters_seen:
            result.append(char*char_count)
            letters_seen.append(char)

    return result