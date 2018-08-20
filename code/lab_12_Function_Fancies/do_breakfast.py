#!/usr/bin/env python
""" Remember this lab solution:
---    
def DoBreakfast(meat="bacon", eggs="over easy", 
                potatos="hash browns", toast="white", 
                beverage="coffee"):
    print "Here is your %s and %s eggs with %s and %s toast." % (
        meat, eggs, potatos, toast)
    print "Can I bring you more %s?" % beverage

DoBreakfast()
DoBreakfast("ham", "basted", "cottage cheese", "cinnamon",
            "orange juice")
DoBreakfast("sausage", toast="white", beverage="chai")
----
Here's an even more flexible way, using the '%' operator
for strings again, but this time with a dictionary
-- as well as variable length keyword calls.
"""
               
def DoBreakfast(**substitutions): 
    order = {'meat':'bacon','eggs':'over easy',
                    'potatos':'hash browns',   
                    'toast':'white','beverage':'coffee'}
    # updating values in order from substitutions
    order.update(substitutions)  
    # string replacement from a dictionary
    print ("Here is your %(meat)s and %(eggs)s eggs with "
           "%(potatos)s and %(toast)s toast."
           "Can I bring you more %(beverage)s?" % order)

def main():
    DoBreakfast()
    DoBreakfast(meat="sausage", toast="wheat", beverage="chai")

if __name__ == '__main__':
    main()
