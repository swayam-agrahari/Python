import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


word = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

if word == "y":
    print(art.logo)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards:
        if sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)


def compare(my_score, computer_score):
    if my_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif my_score == 0:
        return "Win with a Blackjack"
    elif my_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif my_score > computer_score:
        return "You win "
    else:
        return "You lose "


def play_game():
    user_cards = []
    computer_cards = []
    end_of_game = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while (not end_of_game):
        my_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'Your Cards {user_cards}, current score: {my_score}')
        print(f"Computer's first card: {computer_cards[0]}")

        if my_score == 0 or computer_score == 0 or my_score > 21:
            end_of_game = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass:")
            if (user_should_deal == "y"):
                user_cards.append(deal_card())
                computer_cards.append(deal_card())
            else:
                end_of_game = True

    while (computer_score != 0 and computer_score < 17):
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your hand cards:{user_cards} , Your final score: {my_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(my_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print(art.logo)
    play_game()
