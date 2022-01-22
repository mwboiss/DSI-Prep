import random
keep_going = True

while keep_going:
    guess = int(input("Please guess a number between 1 and 100: "))
    random_num = random.randint(1, 100)

    if guess == random_num:
        print("Good guess! You guessed the number correctly!")
    else:
        print(f'WRONG! You guessed {guess} and the number was {random_num}.')

    go_on = input("Would you like to keep playing? Enter y for yes and n for no: ")

    if go_on != 'y':
        keep_going = False
