#!/usr/bin/env python
"""
Demonstrates what happens in the caller when passing in mutable and immutable types.
"""
def Manipulate(this):
    this[1] = "tomatoes"

def TestManipulate(this):
    print ("this = ", this)
    try:
        Manipulate(this)
    except TypeError as msg: # can use "as". msg is provided by exception handler msg. TypeError is an exception class. msg is instantiation of exception class.
        print ("Oops %s broke with %s." % (this, msg))
    else:
        print ("OK. Now we have %s." % this)
        
def main():
    a_list = ["sirloin", "t-bone", "chuck"]
    a_str = "coleslaw"
    a_tuple = ("berries", "peaches", "watermelon")
    a_number = 4.4
    for thing in a_list, a_str, a_tuple, a_number:
        TestManipulate(thing)

if __name__ == "__main__":
    main()
