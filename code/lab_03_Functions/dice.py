#!/usr/bin/env python
"""Rolls dice, demonstrating random.randrange(), and a
tuple with accessing a particular element with an index.
"""

import random  

def Rollem():
    """Rolls a pair of dice and reports the result."""

    DOUBLES = ("Can't happen", "Snake eyes!", "Little joe!",
               "Hard six!", "Hard eight!", "Fever!",
               "Box cars!")

    dice = random.randrange(1, 7), random.randrange(1, 7)
    answer = "%d and %d" % (dice)
    answer += " = %d " % sum(dice)
    if dice[0] == dice[1]:
        answer += DOUBLES[dice[0]]
    return answer

def main():
    while True:
        response = raw_input("Ready to roll? 'q' to quit. ")
        if response and response[0] in "Qq":
            break
        print Rollem()

main()
