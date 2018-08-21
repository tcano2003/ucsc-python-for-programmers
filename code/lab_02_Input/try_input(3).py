#!/usr/bin/env python3
"""Demonstrates catching an exception on error."""

answer = input('What is your favorite number? ')
print ('You like', answer, '?')
print ('You really like ' + answer + '?')
try:               
    number = int(answer)
except ValueError:
    print (answer, 'is not a number!')
else: # this means there is no error
    if number < 10:
        print (number, 'is small.')
    elif number >= 1000:
        print (number, 'is big.')
    else:
        print (number, 'is medium.')

    print ('But you like ' + str(number) + '!')
