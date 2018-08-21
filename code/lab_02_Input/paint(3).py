#!/usr/bin/env python3
"""Demonstrates formatted output, and both uses of '%'
1.  string replacement
2.  modulo
"""   
PER_GALLON = 200      # A can of paint covers 200 square feet
sq_ft = 0 
while sq_ft == 0:
    said = input("Number of square feet to paint: ")
    if not said:   # or if said == '': (This is false)
        print ("Thank you anyway.") 
        break
    try:
        sq_ft = int(said) #sq_ft NOT A VARIABLE, but an IDENTIFIER
    except ValueError:
        print ("Please give a whole number.")
else:
    no_cans = sq_ft/PER_GALLON
    if sq_ft % PER_GALLON > 0:
        no_cans += 1
        print ("You need %.1f cans so you'd better buy" % ( 
            float(sq_ft)/PER_GALLON), end=' ') #%.1f (format of one decimal place)
    else:
        print ("You need exactly", end=' ')
    print ("%d %s." % (no_cans, "can" if no_cans==1 else "cans"))
