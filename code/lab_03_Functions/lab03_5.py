#!/usr/bin/env python
"""Coin flip Experiments, continued. """
from __future__ import division
import random

def FlipCoin():
    """Simulates the flip of a coin."""

    if random.randrange(0, 2) == 0:
        return "tails"
    return "heads"

def GetHeads(target):
    """Flips coins until it gets target heads in a row."""

    heads = count = 0
    while heads < target:
        count += 1
        if FlipCoin() == 'heads':
            heads += 1
        else:          # 'tails'
            heads = 0
    return count

def GetAverage(number_of_experiments, target):
    """Calls GetHeads(target) that number_of_experiments
    times and reports the average."""

    total = 0
    for n in range(number_of_experiments):
        total += GetHeads(target)
    print "Averaging %d experiments, it took %.1f coin flips to get %d in a row." % (number_of_experiments, total/number_of_experiments, target)

GetAverage(100, 3)
