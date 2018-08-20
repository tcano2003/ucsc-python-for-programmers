#!/usr/bin/env python
"""Prints the decimal equivalent of a binary string."""
string = "1011"
for ch in string:
    if ch not in "01":
        print string, 'is not a binary string.'
        break
else:
    answer = 0
    for ch in string:
        answer = 2*answer + int(ch)
    print string, 'in binary is', str(answer) + '.'
    # Python method
    print 'Easy way:', int(string, 2)
