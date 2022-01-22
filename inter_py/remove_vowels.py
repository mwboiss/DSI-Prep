string = 'This is a TEST of a FUNCtion'

def remove_vowels(string):
    remove_me = 'aeiou'
    string_cpy = string
    nw_string = string.lower()
    for char in string:
        if char.lower() in remove_me:
            string_cpy = string_cpy.replace(char, '', nw_string.count(char.lower()))
            print(char)
    return string_cpy
print(remove_vowels(string))

# given option

def remove_vowels(string):
    '''
    Removes all vowels from a string.

    Parameters:
    ----------
    string : (str)
        The string from which vowels should be removed.

    Return:
    ----------
    The string without any vowels.
    '''
    vowels = ['a','A','e','E','i','I','o','O','u','U']

    out = string
    for vowel in vowels:
        out = out.replace(vowel, '')

    return out