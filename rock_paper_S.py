#  Nathan Reid
# Oct. 4th, 2022
# Creating a Rock, Paper, Scissors game

import random

# inform users of directions
print("Here are the directions: \nTwo players will each randomly choose one of three hand signs:")
print("\tRock (made by making a fist),") 
print("\tRaper (made by laying your hand flat), or") 
print("\tScissors (made by holding out two fingers to look like scissors).") 
print("Both players show their signs at the same time to see who will win.")
print("Played in a best-three-out-of-five.\n") 

'''
    Rock wins over scissors (because rock smashes scissors)
    Scissors wins over paper (because scissors cut paper)
    Paper wins over rock (because paper covers rock)
'''
# scoreboard at the start of the game
user_score = 0
computer_score = 0

# flag
active = True

# start game
while active:

    # prompt user for their selection
    user_pick = input("\nWhat do you pick: ")

    # allow user to stop game at anytime
    if user_pick == "quit":
        break

    # have computer to randomly select
    computer_pick = random.randint(1,3)
    
    # game logic
    if computer_pick == 1 and user_pick.title() == 'Scissors':
        print("Computer selects - Rock. Computer Wins")
        computer_score += 1
    elif computer_pick == 2 and user_pick.title() == 'Rock':
        print("Computer selects - Paper. Computer Wins")
        computer_score += 1
    elif computer_pick == 3 and user_pick.title() == 'Paper':
        print("Computer selects - Scissors. Computer Wins")
        computer_score += 1
    elif user_pick.title() == 'Scissors' and computer_pick == 2:
        print("User Wins")
        user_score += 1
    elif user_pick.title() == 'Rock' and computer_pick == 3:
        print("User Wins")
        user_score += 1
    elif user_pick.title() == 'Paper' and computer_pick == 1:
        print("User Wins")
        user_score += 1
    else:
        print("This round was a draw. You and the computer picked the samething.")
    
    # keep score
    print("\nUser's Score: " + str(user_score))
    print("Computer's Score: " + str(computer_score))

    # If user gets to 2 first the game is over
    if user_score == 3:
        print("\nUser wins the GAME!")
        break

    # If user gets to 2 first the game is over
    if computer_score == 3:
        print("\nComputer wins the GAME!")
        break
    