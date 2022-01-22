def menu_func():
    selections_num = []
    selections_name = []
    another_order = True

    while another_order == True:
        menu_string = '''Select from this list:
        1 : bread
        2 : butter
        3 : potatoes
        4 : broccoli'''

        print(menu_string)

        inp = int(input('please make a selection, 1-4: '))

        if inp in [1,2,3,4]:
            selections_num.append(inp)
        else:
            print('-- your selection was not understood --')
            continue

        inp2 = input('would you like to place another order? (y/n)')

        if inp2 == 'y':
            continue
        else:
            for num in selections_num:
                if num == 1:
                    selections_name.append('bread')
                if num == 2:
                    selections_name.append('butter')
                if num == 3:
                    selections_name.append('potatoes')
                if num == 4:
                    selections_name.append('broccoli')
            another_order = False

    return print(f'You ordered: {selections_name}')

print(menu_func())