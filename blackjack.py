# Nathan Reid
# Oct. 24, 2022
# Create a Blackjack game

import random

# players betting money amount total
player_casino_money = 3000

# dealer's cards score total
dealer_score = 0

# player's  cards score total
player_score = 0

# dictionay - representing the card deck
cards = {
    'clubs':[1,2,3,4,5,6,7,8,9,'Jack','Queen','King','Ace'],
    'spades':[1,2,3,4,5,6,7,8,9,'Jack','Queen','King','Ace'],
    'hearts':[1,2,3,4,5,6,7,8,9,'Jack','Queen','King','Ace'],
    'diamonds':[1,2,3,4,5,6,7,8,9,'Jack','Queen','King','Ace'],
}

# put copy of cards in empty list
dealt = [ ]

# dealer pile of cards
dealer_stack = [ ]

# player pile of cards
player_stack = [ ]

# flag
playing = True


# player bet on hand
while playing:
    
    # Make sure the player only enters an integar and not a string
    try:
        wager = int(input("\nHow much are you betting this round? "))
        pass
    except ValueError:
        print("Please enter a number bet ...")

    if wager < player_casino_money:
        print("You are betting " + str(wager) + "!")
        player_casino_money = player_casino_money - wager
        pass
    elif wager >= player_casino_money:
        print("You do not have enough money to bet that amount.")

    # create the card 
    for i in cards.values():
        digit = random.choice(i)
        suit = random.choice(list(cards))
        card = str(digit) + " of " + suit
        print(card)
        # deal the cards out at the start of the round
        dealt.append(card)

    # dealer and player collect their cards
    dealer_stack, player_stack = dealt[:2], dealt[2:4]

    # add numeric value to the dealer's cards while iterating through the stack 
    for card in dealer_stack:
        # print(card)
        if 'Jack' in card:
            card_value = 10
            dealer_score += card_value
        elif 'Queen' in card:
            card_value = 10
            dealer_score += card_value
        elif 'King' in card:
            card_value = 10
            dealer_score += card_value 
        elif 'Ace' in card:
            card_value = 11
            dealer_score += card_value
        else:
            # convert the string into a list and isolate the number from the rest of the string
            num = list(card[0])
            # convert the isolate string number into an integar
            card_num = eval(num[0])
            # make the card score eual the number on the card
            card_value = card_num
            dealer_score += card_value

    print("\n" + str(dealer_score) + " is the dealers hand total.\n")

    # add numeric value to the player's cards while iterating through the stack 
    for card in player_stack:
        # print(card)
        if 'Jack' in card:
            card_value = 10
            player_score += card_value
        elif 'Queen' in card:
            card_value = 10
            player_score += card_value
        elif 'King' in card:
            card_value = 10
            player_score += card_value 
        elif 'Ace' in card:
            card_value = 11
            player_score += card_value
        else:
            # convert the string into a list and isolate the number from the rest of the string
            num = list(card[0])
            # convert the isolate string number into an integar
            card_num = eval(num[0])
            # make the card score eual the number on the card
            card_value = card_num
            player_score += card_value

    print(str(player_score) + " is the players hand total")

    # compare player and dealer score to 21 - the winning score
    if player_score == 21:
        print("Player wins this round. Dealer loses.")
        # Player's bet is times by 2 (* 2) increase it by 100%
        winning_bet = wager * 2
        print("Player won $" + str(winning_bet) + ".")
        player_casino_money = player_casino_money + winning_bet
        print("Player's new total amount to be is $" + str(player_casino_money) + "!")
        break
    elif dealer_score == 21:
        print("Dealer wins this round. Player lose.") 
        player_casino_money = player_casino_money - wager
        print("Player's new total amount is $" + str(player_casino_money))
        break
    elif dealer_score == 21 and player_score == 21:
        print("Game ends in a draw! Player get their money back to bet again.")
        player_casino_money = player_casino_money + wager
        break
    elif dealer_score > 21 and player_score > 21:
        print("Game ends in a draw. Dealer and player score is higher than 21.")
        player_casino_money = player_casino_money + wager
        break


    # NOTE - Don't allow duplicate cards
    # players have the option to hit or stand
    while dealer_score and player_score < 21:
        hand_motion = input("Player would you like to hit or stay? ")
        # check for player's response
        if hand_motion.lower() == 'hit':
            if player_score < 21 and player_score != 21:
                for i in range(1):
                    #card symbols
                    suit = random.choice(list(cards)) 
                    # card numbers
                    digit = random.choice(cards[suit])
                    card_p = str(digit) + " of " + suit
                    if card_p not in player_stack:
                        dealt.append(card_p)
                        player_stack.append(card_p)
                        print("Players new card:")
                        print(card_p)
                        if 'Jack' in card_p:
                            card_value = 10
                            player_score += card_value
                        elif 'Queen' in card_p:
                            card_value = 10
                            player_score += card_value
                        elif 'King' in card_p:
                            card_value = 10
                            player_score += card_value 
                        elif 'Ace' in card_p:
                            card_value = 11
                            player_score += card_value
                        else:
                            num = list(card_p[0])
                            card_num = eval(num[0])
                            card_value = card_num
                            player_score += card_value
                        print("The player new score after the hit is " + str(player_score) + ".")
                
                
                
                if player_score > dealer_score and player_score < 21:
                    continue
                    # print("Player beats the dealer. Player: " + str(player_score) + ", Dealer: " + str(dealer_score))
                    # winning_bet = wager * 2
                    # player_casino_money = player_casino_money + winning_bet
                elif (player_score > dealer_score and player_score > 21) and dealer_score < 21:
                    print("Dealer wins. Dealer: " + str(dealer_score) + " Player: " + str(player_score))
                    player_casino_money = player_casino_money - wager
                elif player_score > dealer_score and player_score == 21:
                    print("Player beats the dealer. Player: " + str(player_score) + ", Dealer: " + str(dealer_score))
                    winning_bet = wager * 2
                    player_casino_money = player_casino_money + winning_bet


            next_round = input("Would you like to play another round? Yes or No ")
            if next_round.lower() == 'yes':
                dealt.clear()
                player_stack.clear()
                dealer_stack.clear()
                player_score = 0
                dealer_score = 0
            elif next_round.lower() == 'no':
                playing = False 

            
        if hand_motion.lower() == 'stay':
            # dealer has the option to 'hit'
            while dealer_score < 21 and dealer_score != 21:
                for i in range(1):
                    # card symbols
                    suit = random.choice(list(cards)) 
                    # card numbers
                    digit = random.choice(cards[suit])
                    card_d = str(digit) + " of " + suit
                    print("Dealers new card:")
                    print(card_d)
                    if card_d not in dealer_stack:
                        dealt.append(card_d)
                        dealer_stack.append(card_d)
                        if 'Jack' in card_d:
                            card_value = 10
                            dealer_score += card_value
                        elif 'Queen' in card_d:
                            card_value = 10
                            dealer_score += card_value
                        elif 'King' in card_d:
                            card_value = 10
                            dealer_score += card_value 
                        elif 'Ace' in card_d:
                            card_value = 11
                            dealer_score += card_value
                        else:
                            num = list(card_d[0])
                            card_num = eval(num[0])
                            card_value = card_num
                            dealer_score += card_value
                        print("The dealer new score after the hit is " + str(dealer_score) + ".")

                if dealer_score > player_score and dealer_score < 21:
                    print("Dealer beats the player. Player: " + str(player_score) + ", Dealer: " + str(dealer_score))
                    player_casino_money = player_casino_money - wager
                elif (dealer_score > player_score and dealer_score > 21) and player_score < 21:
                    print("Player wins. Dealer: " + str(dealer_score) + " Player: " + str(player_score))
                    winning_bet = wager * 2
                    player_casino_money = player_casino_money + winning_bet
                elif dealer_score > player_score and dealer_score == 21:
                    player_casino_money = player_casino_money - wager
                    print("Dealer wins. Dealer: " + str(dealer_score) + " Player: " + str(player_score))

                            
            next_round = input("Would you like to play another round? Yes or No ")
            if next_round.lower() == 'yes':
                dealt.clear()
                player_stack.clear()
                dealer_stack.clear()
                player_score = 0
                dealer_score = 0
            elif next_round.lower() == 'no':
                playing = False 

        

# next round at the end of 'hit' 
# you can continue to hit until you do not want to.
# while hitting if you exceed 21 you bust






                    
            
                
    

    


    


