import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]

# function for clearing the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# create a function to deal cards; pull from 6 decks
def deal_card():
    '''Removes and returns a random card from the 6 decks.'''
    card = cards.pop(random.randrange(len(cards)))
    return card

# create a function to calculate_score(hand)
def calculate_score(hand):
    '''Returns the total of the hand'''
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11) and hand.append(1)
    return sum(hand)

# compare scores
def compare_scores(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw."
    elif dealer_score == 0:
        return "You lose. The dealer has Blackjack."
    elif player_score == 0:
        return "Blackjack! You win."
    elif player_score > 21:
        return "You went over."
    elif dealer_score > 21:
        return "You win! The dealer went over."
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "Sorry, you lose."


def play_blackjack():
    player_cards = []
    dealer_cards = []

    game_on = True

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while game_on:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your hand: {player_cards}, your score: {player_score}")
        print(f"Dealer hand: {dealer_cards}, dealer score: {dealer_score}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_on = False
        else:
            deal_another = input("Would you like another card? 'y' or 'n': ")
            if deal_another == 'y':
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
                print(f"Your hand: {player_cards}, your score: {player_score}")
            else:
                game_on = False

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"The dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare_scores(player_score, dealer_score))

play_blackjack()

while input("Would you like to play again? 'y' or 'n': ") == 'y':
    cls()
    play_blackjack()



