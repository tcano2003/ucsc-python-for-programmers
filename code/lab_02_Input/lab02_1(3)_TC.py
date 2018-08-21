#!/usr/bin/env python3
"""
Asks the user for her name, then asks for the amount of
money she has. It then asks for half the money.
"""
name = input("What is your name? ")
while True:
    try:
        money = float(input("How much money do you have? "))
        break
    except ValueError:
        print("Please try again.")
print("%s, give me $%.2f." % (name, money/2))
