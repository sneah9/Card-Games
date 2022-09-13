import random
names= ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
club= '\u2663'; spade= '\u2660'; heart=  '\u2665'; diamond= '\u2666' #plain suit variables for unicode strings
suits= [club, spade, heart, diamond]

class Card:
    def __init__(self, names, values, suits):
        self.name = names
        self.value = values
        self.suit = suits

class Hand:
    def __init__(self):
        self.cards = []

class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(names, suits):
        deck= []
        for name in names:
            for suit in suits:  
                deck.append(name+suit)
        return deck

    def deck_values(deck):
        values= []
        for value in range(2,15):
            for x in range(4):
                values.append(value)
        key = dict(zip(deck, values))
        return key
