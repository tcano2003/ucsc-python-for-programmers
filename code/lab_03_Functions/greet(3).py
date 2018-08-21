#!/usr/bin/env python3
"""Demonstrates keyword arguments"""

def Greet(first, last): 
    print ('Hello', first, last)

Greet('Rocky','The Squirrel')
Greet(last='Moose', first='Bullwinkle') # the function returns in the correct order

