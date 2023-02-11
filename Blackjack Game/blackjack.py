word = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
def card(guess):
    guess = random.choice(cards)
    return guess

user_cards=[]
computer_cards=[]
for i in  range(2):
    user_cards.append(card)
    computer_cards.append(card)
    
