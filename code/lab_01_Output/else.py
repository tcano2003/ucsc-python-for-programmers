#!/usr/bin/env python
"""Demonstrates if/elif/else and while/else."""

number = 25

if number < 10:
    print number, 'is small'
elif number >= 1000:
    print number, 'is big'
else:
    print number, 'is medium'

if 10 < number < 50:   # "and" is assumed
    print "number is in"
# Alternate syntax since 2.5 -- all one line but less readable.
print number, "is",
print "small" if number < 10 \
              else "big" if number >= 1000 \
              else "medium"  
# else can also occur in a loop
div = 2 
while div * div <= number:   
    if number % div == 0:
        print number, 'is divisible by', div
        break   
    div += 1
else:  
    print number, "is prime"
