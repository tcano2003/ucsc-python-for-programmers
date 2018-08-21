#!/usr/bin/env python3
"""Rolls dice, demonstrating random.randrange(), and a
tuple with accessing a particular element with an index.
"""

import random  

def Rollem():
    """Rolls a pair of dice and reports the result."""

    DOUBLES = ("Can't happen", "Snake eyes!", "Little joe!",
               "Hard six!", "Hard eight!", "Fever!",
               "Box cars!")

    dice = random.randrange(1, 7), random.randrange(1, 7) # tuple is the default
    answer = "%d and %d" % (dice)
    answer += " = %d " % sum(dice) #add on the left and right
    if dice[0] == dice[1]:
        answer += DOUBLES[dice[0]]
    return answer

def main():
    while True:
        response = input("Ready to roll? 'q' to quit. ")
        if response and response[0] in "Qq":
            break
        print (Rollem())

main()
