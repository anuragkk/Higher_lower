import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


print("Welcome to blackjack_game")


def blackjack():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    print(f"Here are your cards: {player_hand[0], player_hand[1]}")
    print(f"Computer's first card is {dealer_hand[0]}")

    # Corrected blackjack condition
    if sum(player_hand) == 21 and sum(dealer_hand) == 21:
        print("Both got blackjack — Game draw!")
        return
    elif sum(player_hand) == 21:
        print(f"You got a blackjack with {player_hand} — You won!")
        return
    elif sum(dealer_hand) == 21:
        print(f"Computer got blackjack with {dealer_hand} — You lost.")
        return

    # Player's turn
    choice = input("Do you want another card? Type 'y' or 'n': ").lower()
    while choice == "y":
        player_hand.append(deal_card())

        # Handle Ace as 1 if needed
        while sum(player_hand) > 21 and 11 in player_hand:
            player_hand[player_hand.index(11)] = 1

        print(f"Your cards now: {player_hand} | Score: {sum(player_hand)}")

        if sum(player_hand) > 21:
            print(f"You lost the game, your cards are {player_hand}")
            return
        elif sum(player_hand) == 21:
            print(f"You hit blackjack, you won! Cards are {player_hand}")
            return

        choice = input("Do you want another card? Type 'y' or 'n': ").lower()

    # Dealer's turn after player stands
    while sum(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        while sum(dealer_hand) > 21 and 11 in dealer_hand:
            dealer_hand[dealer_hand.index(11)] = 1

    print(f"\nYour final hand: {player_hand} | Score: {sum(player_hand)}")
    print(f"Dealer's final hand: {dealer_hand} | Score: {sum(dealer_hand)}")

    # Outcome
    if sum(dealer_hand) > 21:
        print("Dealer busted — You win!")
    elif sum(dealer_hand) > sum(player_hand):
        print("Dealer wins.")
    elif sum(dealer_hand) < sum(player_hand):
        print("You win!")
    else:
        print("It's a draw!")


blackjack()
