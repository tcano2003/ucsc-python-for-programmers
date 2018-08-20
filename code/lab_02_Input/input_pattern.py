#!/usr/bin/env python
"""Demonstrates raw_input in a while loop."""
     
while True: # True/False are keywords.   
    answer = raw_input('What is your favorite number? ')
    try:  
        number = int(answer)
    except ValueError:
        print answer, 'is not a number! Please try again.'
    else:
        break
print "I got your %d!" % (number) # string formatting is
                                  # our next topic
