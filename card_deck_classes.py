import random

class Card:
    def __init__(self, value, suit):  # value between 1 and 14 inclusive. suit as string -> "Diamonds"
        self.value = value
        self.suit = suit

    def __str__(self):  # prints card
        value = self.value
        if value == 1:
            value = "Ace"
        elif value == 11:
            value = "Jack"
        elif value == 12:
            value = "Queen"
        elif value == 13:
            value = "King"
        return f"{value} of {self.suit}"

class Deck:
    def __init__(self):  # builds a deck of cards
        self.deck = []
        suits = ["diamonds", "clubs", "hearts", "spades"]
        for value in range(1,14):
            for suit in suits:
                self.deck.append(Card(value, suit))

    def __str__(self):  # prints deck
        cards = ""
        for card in self.deck:
            cards += str(card) + "\n"
        return cards

    def draw_card(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)  # pop() removes the item at a given index and returns the removed item

    def add(self, other):  # adds cards or other decks
        if type(other) == Card:  # adds a card to the deck
            self.deck.append(other)
        elif type(other) == Deck:  # adds another deck to the deck
            self.deck.extend(other.deck)  # self.deck = self.deck + other.deck also works
        return self

    def shuffle(self):
        random.shuffle(self.deck)  # shuffle() is a method of the random class. It reorganizes items in a sequence.
        return self


deck = Deck()
deck2 = Deck()

deck.add(deck2)  # adds deck2 to deck
deck.shuffle()  # shuffles deck

print(deck.draw_card())  # draws card from deck and prints it
