#!/usr/bin/env python
"""
Asks the user for her name, then asks for the amount of
money she has. It then asks for half the money.
"""
name = raw_input("Name please: ")
while True:  
    try:  
        money = float(raw_input("How much money do you have? "))
        break
    except ValueError:
        print "Please try again."

print "%s, give me $%.2f." % (name, money/2)
