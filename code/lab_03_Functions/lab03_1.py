#!/usr/bin/env python
"""A coin flipping emulation. """
import random

def FlipCoin():
    """Simulates the flip of a coin."""

    if random.randrange(0, 2) == 0:
        return "tails"
    return "heads"

def main(num_times):
    """Driver for testing."""
    heads = 0
    for n in range(num_times):
        if FlipCoin() == "heads":
            heads += 1
    print 'With %d flips, "heads" came up %d times, or' % (
        num_times, heads),
    print '%.1f%% of the flips.' % ((heads * 100.)/num_times)

main(100)
