#!/usr/bin/env python3
"""The "assert" statement is useful while debugging.  It goes
away under any optimization."""  

def main():
    number = float(input("Give me a positive number: "))

    assert number > 0, "Input is not positive: %d" % number

    print ("Good. %s is positive." % number)

if __name__ == '__main__':
    main()

