#!/usr/bin/env python
"""Demonstrates reading a file line by line."""

def PrintFile(f_name): 
    open_file = open(f_name)   
    for line in open_file:   
        print line,
    open_file.close()

def main(f_name):
    PrintFile(f_name)

if __name__ == '__main__':
    main("ram.tzu")
