#!/usr/bin/env python3
"""This is a function that returns heads or tails like the flip of a coin"""
import random

def FlipCoin():
    coin = random.randrange(0, 2)
    if coin == 1:
        print("heads")
    else:
        print("tails")

FlipCoin()
