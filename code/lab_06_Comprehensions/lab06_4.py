#!/usr/bin/env python
"""Use list comprehensions to make a deck of cards.  Print them comma separated except stick in an "and" before the last.
"""

def GetCards():
    """Return a deck of cards as a list of strings."""
    values = [str(x) for x in range(2, 11)
              ] + ['Jack','Queen','King','Ace']
    suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades') 
    deck = ['%s of %s' % (value, suit) for suit in suits
			for value in values] + ["Joker"] * 2
    return deck

def main():
    deck = GetCards()
    print ', '.join(deck[:-1]) + ", and " + deck[-1] + "."
    
if __name__ == '__main__':
    main()
