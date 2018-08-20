#!/usr/bin/env python
"""
lab02_2.py Asks the user for a number to multiply by itself,
and asks the user for the number of digits beyond the decimal
point to display, and gives the answer.
"""
while True:
    number_str = raw_input("Number to square please: ")
    try:
        number = float(number_str)
    except ValueError:
        print "Please try again."
    else:
        break

while True:
    try:
        right_of_decimal = int(raw_input(
"""How many digits to the right of the decimal place would
you like to have displayed? """ ))
    except ValueError:
        print "Please try again."
    else:
        break
        
print "%s squared is %.*f." % (number_str, right_of_decimal,
                               number * number)
