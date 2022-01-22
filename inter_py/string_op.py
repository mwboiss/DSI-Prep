string = 'THis iS AN ExamPLe'
command = 'CAPitalize'

def string_op(string, command):
    command_list = ['upper','lower','capitalize']
    command_low = command.lower()
    nw_str = []
    if command_low not in command_list:
        nw_str = "Invalid command!"
    elif command_low == 'upper':
        nw_str = string.upper()
    elif command_low == 'lower':
        nw_str = string.lower()
    else:
        nw_str = string.capitalize()
    return nw_str

print(string_op(string, command))