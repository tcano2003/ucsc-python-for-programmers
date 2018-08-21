#!/usr/bin/env python3
"""Write a DoBreakfast function that takes five arguments:
meat, eggs, potatos, toast, and beverage.  The default
meat is bacon, eggs are over easy, potatos is hash browns,
toast is white, and beverage is coffee.

The function prints:

Here is your bacon and scrambled eggs with home fries
and rye toast.  Can I bring you more milk?

Call it at least 3 different times, scrambling the arguments.
"""

def DoBreakfast(meat="bacon", eggs="over easy", 
              potatos="hash browns", toast="white", 
              beverage="coffee"):
    print ("Here is your %s and %s eggs with %s and %s toast." % (
        meat, eggs, potatos, toast))
    print ("Can I bring you more %s?" % beverage)

def main():
    DoBreakfast()
    DoBreakfast("ham", "basted", "cottage cheese",
                "cinnamon", "orange juice")
    DoBreakfast("sausage", beverage="chai", toast="wheat")

main()
