#!/usr/bin/env python
"""lab19_3.py Print the names of people born in March."""
import re
import norma  # to collect the data

def BornIn(month, text):
    return re.findall(
        r"""^([^:]+)   # capture the name
        (?::[^:]+)     # don't capture colon followed
        {2}            # non-colons by twice.
        :%s            # follwed by colon and month number
        """ % month, text, re.MULTILINE|re.VERBOSE)

def main():
    print '\n'.join(BornIn(3, norma.ReadFile('address.data')))

if __name__ == '__main__':
    main()

