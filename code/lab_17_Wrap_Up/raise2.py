#!/usr/bin/env python
"""And, you can re-raise an exception."""

import raise1

def main():
    try:
        number = raise1.GetPositiveNumber("Positive number: ")
    except ValueError:
        print "That was wrong!"
        raise    # Raises last exception again

main()
