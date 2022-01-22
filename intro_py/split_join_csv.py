csv_data = "512.8,742.3,532.6,156.9,126.1,987.4,398.7,651.5,4,4.5\n2"

def csv_sqr_csv_mine(csv):
    list_lines = []
        
    for line in csv.split('\n'):
        lines = []
                
        for num in line.split(','):
            
            # this didn't work
            """
            if num.count(".") == 1:
                num = float(num)
                num = num**2
                num = "{:.1f}".format(num)
                num = str(num)
                lines.append(num)
        
            elif num in "0123456789":
                num = int(num)
                num = int(num**2)
                num = str(num)
                lines.append(num)
        
            else:
                lines.append(num)
            """
            if '.' in num:
                lines.append(str(round(float(num)**2, 2)))
        
            else:
                lines.append(str(int(num)**2))
                
        list_lines.append(','.join(lines))
    return '\n'.join(list_lines)
"""

# vid example
"""
def csv_sqr_csv_vid(string):
    new_list_lines = []

    for line in string.split('\n'):
        new_line = []

        for val in line.split(','):
    
            if '.' in val:
                new_line.append(str(round(float(val)**2 , 2)))
    
            else:
                new_line.append(str(int(val)**2))
    
        new_list_lines.append(','.join(new_line))
    return '\n'.join(new_list_lines)


# given example

def csv_sqr_csv_given(csv_data):
    # Initialize a collector for the data lines
    lines = []

    for line in csv_data.split("\n"):
        # Initialize a collector for each item in the data line
        squared_nums = []

        for num in line.split(","):
            # Check if 'num' contains only digits and cast
            # to 'int' if so, otherwise cast to 'float'
            # e.g.: 125.0 vs 125
            if num.isdigit():
                n = int(num)
            else:
                n = float(num)

            # Now square the number and round to two places
            n_squared = round(n**2, 2)

            # Cast to 'str' and append to the 'squared' collector
            squared_nums.append(str(n_squared))

        # Append the new data line to the 'lines' collector
        lines.append(",".join(squared_nums))

    # Finally, rejoin the data lines with the newline character
    return "\n".join(lines)

print(csv_data)
print('\n')
print(csv_sqr_csv_mine(csv_data))
print('\n')    
print(csv_sqr_csv_vid(csv_data))
print('\n')
print(csv_sqr_csv_given(csv_data))