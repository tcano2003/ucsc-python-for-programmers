#!/usr/bin/env python
"""
Write a function that reads a file and finds all the
numbers in the file and adds them up. 
"""

import sys, os

# putting apple on the search path -- robust method            
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))

import banana.total_text     # banana must have __init__.py

def TotalIt(stream, total=0):
    """Returns the sum of all the numbers in stream, which is 
    an open file object."""
    for line in stream:
        total += banana.total_text.TotalText(line)
    return total

def TotalFile(file_name):
    """Returns the sum of all the numbers in the file."""
    try:
        open_file = open(file_name)
        try:
            return TotalIt(open_file)
        finally:
            open_file.close()
    except IOError:
        print "I can't read '%s'." % (file_name)

def main():
    while True:
        try:
            file_name = raw_input('File name: ')
        except (KeyboardInterrupt, EOFError):
            print
            break
        if file_name == '':
            break
        total = TotalFile(file_name)
        if total:
            print file_name, 'totals to', total

if __name__ == '__main__':
    main()

