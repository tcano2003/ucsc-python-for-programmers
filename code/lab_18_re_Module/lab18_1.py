#!/usr/bin/env python
"""lab18_1.py Finds and adds up all the numbers in a file."""
import re

number_finder = re.compile(r"""
\d*       # maybe some digits
\.        # a dot
\d+       # and one or more digits
|         # or
\d+       # just some digits
""", re.VERBOSE) # re.VERBOSE flag allows all those comments

def TotalLine(line):
    """Returns the sum of all the numbers in the line."""
    # print number_finder.findall(line)
    return sum([float(each) for each in 
                number_finder.findall(line)])

def TotalIt(open_file_like_object):
    """Returns the sum of all the numbers in the 
    open_file_like_object.
    """
    return sum([TotalLine(line) for line in open_file_like_object])

def TotalFile(name):
    """Returns the sum of all the numbers in the file."""
    try:
        open_file = open(name)
        try:
            return TotalIt(open_file)
        finally:
            open_file.close()
    except IOError:
        print "I can't read '%s'." % (name)

def main():
    while True:
        try:
            name = raw_input('File name: ')
        except (KeyboardInterrupt, EOFError):
            print
            break
        if name == '':
            break
        total = TotalFile(name)
        if total:
            print name, 'totals to', total

if __name__ == '__main__':
    main()

