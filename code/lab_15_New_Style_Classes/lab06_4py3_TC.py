#!/usr/bin/env python3
"""Use list comprehensions to make a deck of cards.  Print them comma separated except stick in an "and" before the last.
"""

def GetCards():
    """Return a deck of cards as a list of strings."""
    values = [str(x) for x in range(2, 11) #cards from 2-10
              ] + ['Jack','Queen','King','Ace'] 
    suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades') #tuple of the suits 
    deck = ['%s of %s' % (value, suit) for suit in suits #list of strings
			for value in values] + ["Joker"] * 2 
    return deck

def main():
    deck = GetCards()
    print (', '.join(deck[:-1]) + ", and " + deck[-1] + ".") #join all cards except the last, add and and call last card in deck.
    
if __name__ == '__main__':
    main()
