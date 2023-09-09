# Nathan Reid
# Oct. 10th, 2022
# Create a number guessing game

import random

# provide the directoins to the player.
print('''Guess the correct number the computer randomly picked. \nContinue to guess until you choose the correct number.
No negative numbers.\nChoose from 0 - 14.''')

# create the computer pick and allow them to pick first
computer_num = random.randint(0,14)

# use a flag for the game
active = True

# prompt the player to choose a number. Convert the string to an integar
user_selection = int(input("\nPick what number the computer has selected: "))

# Keep track of how many guess to get the right number
attempts = 0

# Use a while loop to start and end the game
while active:

    # game logic
    # check to see if the computer number and user number is the same
    if user_selection == computer_num:
        print("\nThe computer selected > " + str(computer_num) + ".")
        print("You guessed " + str(user_selection) + ".")
        print("You have choose the correct number! Good Job!")
        print("It took you " + str(attempts) + " attempt(s) to guess the right number.")
        break
    # wrong user number
    if user_selection != computer_num:
        # check to see if the user number is too high or too low
        if computer_num > user_selection:
            print("\nIncorrect. Choose higher.")
            user_selection = int(input("Guess again: "))
            attempts += 1
        elif computer_num < user_selection:
            print("\nIncorrect. Choose lower.")
            user_selection = int(input("Guess again: "))
            attempts += 1
        