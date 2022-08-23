class deck:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def create_deck():
    deck= []
    for suit in ['\u2663', '\u2660', '\u2665', '\u2666']:# define variables for unicode strings as hearts...
        for card in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:  
            deck.append(card+suit)
    return deck

    def deck_values():
    values= []
    for x in range(4):
        for value in range(2,15):
            values.append(value)
    key = dict(zip(deck, values))
    return key