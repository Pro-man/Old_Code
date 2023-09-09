# Nathan Reid
# Oct. 7th, 2022
# Create Tic-Tac-Toe game

# import random module for computer player
import random

# display directions of game
print('''Game Directions:
    This game is played between two players.
    You can select from X or O.
    Enter your selection on a spot on the board.
    The first players to reach three marks in a row wins.
    If no player does not get three sections in a row, 
    the game ends in a draw.
    ''')

# create the game board
board = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# display game board visual for user
print('''Game Board
A1 | A2 | A3
_____________
B1 | B2 | B3
_____________
C1 | C2 | C3
''')

# empty list for x player moves
x = [ ]

# empty list for o player moves
o = [ ]

# winning order nested list
winning_order = [['A1', 'A2', 'A3'],
['A3', 'A2', 'A1'],
['C1', 'C2', 'C3'],
['C3', 'C2', 'C1'],
['A1', 'B1', 'C1'],
['C1', 'B1', 'A1'],
['A3', 'B3', 'C3'],
['C3', 'B3', 'A3'],
['A1', 'B2', 'C3'],
['C3', 'B2', 'A1'],
['A3', 'B2', 'C1'],
['C1', 'B2', 'A3'],
['B1', 'B2', 'B3'],
['B3', 'B2', 'B1']]

# flag for the game
active = True

# create game with a while loop
while active:

    # prompt user to pick which section to place an X on board
    user_pick = input("\nWhere do you want to mark your X? ")

    # allow user to end game 
    if user_pick.title() == 'Quit':
        break
 
    # NOTE - del is not a function, it is a keyword to create del statements 
    # e.g. del var. You can't use it as a function or on a function,

    # mark X the spot the user picks
    if user_pick in board:
        board.remove(user_pick)
        x.append(user_pick)
    else:
        # check to see if the user picked a previous marked spot by them or computer
        re_pick = input("That spot is taken. Pick another. ")
        board.remove(re_pick)
        x.append(re_pick)

    # iterate through list and check the elements for the winning order
    for order in winning_order:
        # order are the lists in the list [B3, B2, B1]
        for i in order:
            # i is B3( are all the elements)
            if order == o:
                active = False
                print("Three O's in a row. Computer won!")
                # break stop the print displaying three times for each element in the list
                break
            elif order == x:
                print("Three X's in a row. User won!")
                active = False
                break

    # computer turn to pick:
    if active:
        # create computer pick
        cp = random.choice(board)
        print("The computer has put an O on space: " + cp)
        board.remove(cp)
        o.append(cp)
        # check to see if any spots are open on the board. If not end game in a draw.
    elif len(board) == 0:
        print("This game ends in a draw. Play again.")
        break


