#!/usr/bin/env python3
"""Demonstrates reading a file line by line."""

def PrintFile(f_name): 
    open_file = open(f_name)   
    for line in open_file: #for char in open_file.read(1): -- read one character at a time  
        print (line, end='')
    open_file.close()

def main(f_name):
    PrintFile(f_name)

if __name__ == '__main__':
    main("ram.txt")
