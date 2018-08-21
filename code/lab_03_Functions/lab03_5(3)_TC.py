#!/usr/bin/env python3
"""This is a function that returns heads or tails like the flip of a coin"""
import random

def FlipCoin():
    if random.randrange(0, 2) == 0:
        return ("tails")
    return ("heads")
    
def GetHeads(target):
    """Flips coins until it gets target heads in a row."""

    heads = count = 0
    while heads < target:
        count += 1
        if FlipCoin() == 'heads':
            heads += 1
            # print("heads") test code to show when heads occurs
        else:          # 'tails'
            heads = 0
            # print("tails") test code to show when tails occurs
    return count

def GetAverage(number_of_experiments, target):
    """Calls GetHeads(target) that number_of_experiments
    times and reports the average."""

    total = 0
    for n in range(number_of_experiments):
        total += GetHeads(target)
    print ("Averaging %d experiments, it took %.1f coin flips to get %d in a row." % (number_of_experiments, total/number_of_experiments, target))

GetAverage(100, 3)
