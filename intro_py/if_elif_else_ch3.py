def depends_on_the_type(obj):
    if type(obj) == int:
        
        if obj == 0:
            return f'Zero'
        
        elif obj % 2 == 0:
            return obj ** 2
        
        else:
            return obj ** 3

    elif type(obj) == float:
        return obj * 1.5

    elif type(obj) == str:
        return f'{obj} {obj}'

    elif type(obj) == bool:
        return not obj

    else:
        return f'None'

print(depends_on_the_type(5))