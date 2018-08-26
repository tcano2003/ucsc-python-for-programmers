#!/usr/bin/env python3
"""(Optional)An iterating Deck of cards.
"""
import os, random, sys
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))

import lab06_4py3_TC as cards

class Deck:
    """An iterating deck of cards that destroys each card 
    as it is taken with a next call - or as it is iterated
    with a for-loop."""

    def __init__(self): #self is deck
        self.__cards = cards.GetCards() # secret cards
        random.shuffle(self.__cards)

    def __iter__(self): # return deck. Magic iterator is for faciliting: enumerate, sort, or do partially. Next too.
        return self

    def next(self):
        try:
            return self.__cards.pop() # remove card and return the value
        except IndexError:
            raise StopIteration

class Player:
    def __init__(self):
        self.hand = [] #open an empty list [empty hand]

    def AcceptCard(self, card):
        self.hand += [card] #add card to hand?

    def __str__(self):
        return ', '.join(self.hand) #gets a hand, return passed cards as a string

class GameDealer:
    def __init__(self, no_players=4, no_cards=5):
        self.no_cards = int(no_cards)
        self.players = [Player() for p in range(int(no_players))] #order of dealing the cards
        self.deck = Deck()
        self.DealHands()



        
    def DealHands(self):
        """Deals cards to the players."""
        for card_no in range(self.no_cards): #deal one card to each player
            for player in self.players:
                try:
                    new_card = self.deck.next() #another round of dealing. Could do in for loop and break out? No, would possibly restart
                except StopIteration:
                    new_card = "Sorry" # no cards left to deal
                player.AcceptCard(new_card)

    def __str__(self):
        """Returns a string representation of the dealt
        cards."""
        return  '\n'.join([str(p) for p in self.players]) # str(p) is the player's hand of cards

def main():
    for players, cards in ((4, 5), (20, 3)):
        print ("GameDealer(%d, %d)" % (players, cards))
        print (GameDealer(players, cards))

if __name__ == '__main__':
    main()
