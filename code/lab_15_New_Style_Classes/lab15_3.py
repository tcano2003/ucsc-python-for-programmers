#!/usr/bin/env python
"""(Optional)An iterating Deck of cards.
"""
import os, random, sys
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))

import lab_06_Comprehensions.lab06_4 as cards

class Deck:
    """An iteratiing deck of cards that destroys each card 
    as it is taken with a next call - or as it is iterated
    with a for-loop."""

    def __init__(self):
        self.__cards = cards.GetCards()
        random.shuffle(self.__cards)

    def __iter__(self):
        return self

    def next(self):
        try:
            return self.__cards.pop()
        except IndexError:
            raise StopIteration

class Player:
    def __init__(self):
        self.hand = []

    def AcceptCard(self, card):
        self.hand += [card]

    def __str__(self):
        return ', '.join(self.hand)

class GameDealer:
    def __init__(self, no_players=4, no_cards=5):
        self.no_cards = int(no_cards)
        self.players = [Player() for p in range(int(no_players))]
        self.deck = Deck()
        self.DealHands()



        
    def DealHands(self):
        """Deals cards to the players."""
        for card_no in range(self.no_cards):
            for player in self.players:
                try:
                    new_card = self.deck.next()
                except StopIteration:
                    new_card = "Sorry"
                player.AcceptCard(new_card)

    def __str__(self):
        """Returns a string representation of the dealt
        cards."""
        return  '\n'.join([str(p) for p in self.players])

def main():
    for players, cards in ((4, 5), (20, 3)):
        print "GameDealer(%d, %d)" % (players, cards)
        print GameDealer(players, cards)

if __name__ == '__main__':
    main()
