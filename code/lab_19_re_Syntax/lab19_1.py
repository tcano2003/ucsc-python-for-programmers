#!/usr/bin/env python
"""lab19_1.py Change "CA" to "California"."""
import re
import norma  # to collect the data

def WholeCa(text):
    return re.sub(r"\bCA\b", "California", text)

def main():
    print WholeCa(norma.ReadFile('address.data'))

if __name__ == '__main__':
    main()

