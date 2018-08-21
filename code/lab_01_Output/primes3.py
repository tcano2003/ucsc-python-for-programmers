#!/usr/bin/env python
"""Produces a list of prime numbers > 2.

Here, we are only checking the "look" of Python code.
"""
MAX = 100             # Here is a comment.   

print ('primes less than', MAX, 'are:') # A new line is added
                                      # by default.

for number in range(3, MAX, 2):
    div = 2
    while div * div <= number:
        if number % div == 0: 
            break     
        div += 1      
    else:             # Overloaded 'else', loop didn't 'break'.
        print (number, end=' ') # Trailing comma suppresses the new line.
print()                 # This only produces the new line.
