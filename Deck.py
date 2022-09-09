import random
names= ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
club= '\u2663'; spade= '\u2660'; heart=  '\u2665'; diamond= '\u2666' #plain suit variables for unicode strings
suits= [club, spade, heart, diamond]

class cards:
    def __init__(self, names, suits):
        self.name = names
        self.suit = suits

def create_deck(names, suits, shuffled=False):
    deck= []
    for name in names:
        for suit in suits:  
            deck.append(name+suit)
    if shuffled == True:
        random.shuffle(deck)
    return deck

def deck_values():
    values= []
    for x in range(4):
        for value in range(2,15):
            values.append(value)
    key = dict(zip(cards, values))
    return key

deck1= create_deck(names, suits, shuffled=False);

print (deck1);