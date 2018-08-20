#!/usr/bin/env python
"""lab19_6.py Print the file with the first and last names
reversed.
"""
import re
import norma  # to collect the data

def ReverseNames(text):
    compiled_re = re.compile(
        r"^(?P<name>[^:]+):", re.MULTILINE)
    def DoTheReverse(match_object):
        try:
            first, last = match_object.group("name").rsplit(None,
                                                            1)
        except ValueError:
            return match_object.group()
        return last + ', ' +  first + ':'
    return compiled_re.sub(DoTheReverse, text)

def main():
    print ReverseNames(norma.ReadFile('address.data'))

if __name__ == '__main__':
    main()

