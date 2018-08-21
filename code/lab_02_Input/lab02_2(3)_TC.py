#!/usr/bin/env python3
"""
lab02_2.py Asks the user for a number to multiply by itself,
and asks the user for the number of digits beyond the decimal
point to display, and gives the answer.
"""
while True:
    userinput = input("Number to square please: ")
    try:
        number = float(userinput)
    except ValueError:
        print("Please try again.")
    else:
        break

while True:
    try:
        digitstoright = int(input("How many digits to the right of the decimal place would you like to have displayed? "))
    except ValueError:
        print("Please try again.")
    else:
        break

print("%s squared is %.*f." % (userinput, digitstoright, number * number))
