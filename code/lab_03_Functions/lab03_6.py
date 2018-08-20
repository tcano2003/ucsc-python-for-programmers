#!/usr/bin/env python
"""Introspect the random module, and particularly the randrange()
function it provides.  Use this module to write a "Flashcard"
function.  Your function should ask the user:

What is 9 times 3

where 9 and 3 are any numbers from 0 to 12, randomly chosen.

If the user gets the answer right, your function should print
"Right!" and then return a 1.  If the answer is wrong, print
"Almost, the right answer is 27" and return a 0.

Write a function called TestAndScore(n) that calls your
Flashcard function n times and prints the percentage of right
answers like this, "Score is 90". It also returns this
percentage.

Make another function called GiveFeedback(p) that receives a
percentage, 0 - 100.  If p is 100 it prints "Perfect!", if it's
90-99 it prints "Excellent", 80-89 prints "Very good", 70-79
prints "Good enough", and  <= 69, "You need more practice".

Test all that in your program, calling TestAndScore(10) and
then pass the returned value into GiveFeedback().

Make a new function called "Praise" that takes no arguments.
It prints one of (at least) 5 phrases of Praise, chosen
randomly.  It might print, "Right On!", or "Good work!",
for example.  Call this Praise() function from your
Flashcard() function whenever your user gets the answer right.
"""
import random
def FlashCard():
    n1 = random.randrange(13)
    n2 = random.randrange(13)
    answer = n1 * n2
    print "What is %d times %d? " % (n1, n2)
    while True:
        try:
            response = int(raw_input())
        except ValueError:
            print "%d times %d is a number.  What number? " % (
                n1, n2)
            continue  
        if response == answer:
            print "Right!",
            Praise()
            return 1
        print "Almost, the right answer is %d." % answer
        return 0

def GiveFeedback(p):
    if p == 100:
        print 'Perfect!'
    elif p >= 90:
        print 'Excellent'
    elif p >= 80:
        print 'Very good'
    elif p >= 70:
        print 'Good enough'
    else:
        print 'You need more practice'

def Praise():
    pats = ("That's great!", "You're right!",
            "Good work!", "Right On!", "Superb!")
    print random.choice(pats)

def TestAndScore(n):
    score = 0
    for time in range(n):
        score += FlashCard()
    score =  int(100.0 * score/n)
    print "Score is %d." % score
    return score

GiveFeedback(TestAndScore(10))

