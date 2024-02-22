import random

# Define card ranks, suits, and values
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<card hidden>")
    print(dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(player, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts! Player wins!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push.")

class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed {chips.total}")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal_card())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        choice = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
        if choice[0].lower() == 'h':
            hit(deck, hand)
        elif choice[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break


def main():
    global playing
    print("Welcome to Blackjack!")

    while True:
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()
        player_chips = Chips()

        take_bet(player_chips)

        # Deal initial cards
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        show_some(player_hand, dealer_hand)

        while playing:
            hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                player_busts(player_hand, player_chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        print("\nPlayer's winnings stand at", player_chips.total)

        new_game = input(
            "Would you like to play another hand? Enter 'y' or 'n': ")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    playing = True
    main()