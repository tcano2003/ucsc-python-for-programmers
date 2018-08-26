#!/usr/bin/env python3
"""Demonstrating the sys module.""" 

import sys 
           
def DemoOpenStreams():
    """Demos stderr, stdout and stdin.  Also sys.exit()"""
    sys.stderr.write('You can write to stderr.\n')
    print (>> sys.stderr, "You might like the >> syntax.") # look this up how to convert to Python 3
    sys.stdout.write('A fancier way to write to stdout.\n')
    print ('Type something: ')
    text = sys.stdin.readline()
    print ('You said:', text)

def DemoCommandLine(): 
    """Shows the command line."""
    print ('This program is named:', sys.argv[0]) #arg vector
    print ('The command line arguments are:', sys.argv[1:])

def main():
    DemoCommandLine()
    DemoOpenStreams()
main()

