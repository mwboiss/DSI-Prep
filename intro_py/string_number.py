def is_number(string):
    if not string or string.count(".") > 1: 
        return "Not a number"
    for char in string:
        if char not in ".0123456789":
            return "Not a number"
    if string.count(".") ==1:
        return "float"
        
    return "int"

# option given

def is_number(string):
    # Edge-case handling for empty strings and strings with 2+ decimals
    if not string or string.count(".") > 1:
        return "Not a number"

    # Check each character to make sure it's either a digit or a decimal point
    for char in string:
        if char not in ".0123456789":
            return "Not a number"

    # Either an int or a float, depending on how many decimal points there are
    if string.count(".") == 0:
        return "int"
    return "float"