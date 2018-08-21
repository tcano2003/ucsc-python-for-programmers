#!/usr/bin/env python3
"""Write a function that returns a total cost from the 
sales price and sales tax.  The default value for the 
tax rate should be 8.25%"""

def DoBreakfast(meat = "bacon", eggs ="over easy", potatoes = "hash browns",
                toast = "white", beverage = "coffee"):
    print("Here is your", meat, "and", eggs, "eggs with", potatoes, "and", toast, "toast. Can I bring you some more", beverage, "?")

DoBreakfast()
DoBreakfast("sausage", "scrambled", "mashed potatoes", "sourdough", "orange juice")
DoBreakfast("ham", "hard-boiled", "baked potato", "wheat", "milk")
DoBreakfast("turkey", "raw", "fries", "cornbread", "apple juice")
