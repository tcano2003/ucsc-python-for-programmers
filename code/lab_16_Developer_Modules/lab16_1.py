#!/usr/bin/env python
"""(Optional) Test for GameDealer class."""

import unittest

import os, sys
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
    
import lab_15_New_Style_Classes.lab15_3 as game_dealer

WHOLE_DECK = sorted(game_dealer.Deck())

class ReportingDealer(game_dealer.GameDealer):
    """GameDealer only had methods that output strings,
    so here we provide a list version for testing.
    """
    def Report(self):
        """For testing."""
        return [p.hand for p in self.players]

class TestPlayCards(unittest.TestCase):

    def testSmall(self):
        little = ReportingDealer(1, 1).Report()
        self.assertEqual(len(little), 1)
        self.assertEqual(len(little[0]), 1)
        self.assert_(little[0][0] in WHOLE_DECK)

    def testZilch(self):
        self.assertEqual([], ReportingDealer(0, 1).Report())
        self.assertEqual([[]], ReportingDealer(1, 0).Report())
        self.assertEqual([], ReportingDealer(0, 0).Report())

    def testWholeDealer(self):
        all_hands = ReportingDealer(9, 6).Report()
        for hand in all_hands:
            self.assertEqual(len(hand), 6)
        self.assertEqual(len(all_hands), 9)
        all_hands_collapsed = reduce(lambda x,y: x + y, all_hands)
        all_hands_collapsed.sort()
        self.assertEqual(all_hands_collapsed, WHOLE_DECK)




        
    def testTooMany(self):
        too_many = ReportingDealer(11, 5).Report()
        too_many_collapsed = reduce(lambda x,y: x + y,
                                    too_many)
        self.assert_('Sorry' in too_many_collapsed)
        too_many_collapsed.remove('Sorry')
        too_many_collapsed.sort()
        self.assertEqual(too_many_collapsed, WHOLE_DECK)

    def testWayTooMany(self):
        way_too_many = ReportingDealer(11, 6).Report()
        way_too_many_collapsed = reduce(lambda x,y: x + y,
                                        way_too_many)
        self.assertEqual(len(way_too_many_collapsed), 66)
        self.assertEqual(way_too_many_collapsed.count('Sorry'),
                         12)
        for i in range(12):
            way_too_many_collapsed.remove('Sorry')
        way_too_many_collapsed.sort()
        self.assertEqual(way_too_many_collapsed, WHOLE_DECK)

if __name__ == '__main__':
    unittest.main()

