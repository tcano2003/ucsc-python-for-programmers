#!/usr/bin/env python
"""Demonstrates keyword arguments"""

def Greet(first, last): 
    print 'Hello', first, last

Greet('Rocky','The Squirrel')
Greet(last='Moose', first='Bullwinkle')

