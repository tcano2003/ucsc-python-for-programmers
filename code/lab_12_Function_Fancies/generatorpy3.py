#!/usr/bin/env python3
"""Function to generate random numbers without repetition.
Demonstrates generators and the 'yield' keyword."""
import random 

def Harvest():
    yield "potatos" # yield denotes generator function. This makes generator object
    yield "corn"
    yield "peas"

def DemoHarvest():
    for crop in Harvest():
        print (crop, end='')
    print()
    
def Unique(bot, over_top):
    """Generator to deliver randomly chosen values from bot
    to over_top - 1, delivering each value once only."""
    answers = range(bot, over_top)
    random.shuffle(answers)
    for each in answers:
        yield each

def ListUnique(bot, over_top):
    """Returns a list of the generated numbers
    """
    gen = Unique(bot, over_top)
    while True:
        try:
            print (gen.next(), end='')
        except StopIteration:
            return

def ListUnique(bot, over_top):
    """Same action! """
    for number in Unique(bot, over_top):
        print (number, end='')
    print()
if __name__ == '__main__':
    DemoHarvest()
    print ('ListUnique(10, 21) --> ', end='')
    ListUnique(10, 21)
