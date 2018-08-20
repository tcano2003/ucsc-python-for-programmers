#!/usr/bin/env python
"""Interactive 2-D string unwrapper.
"""
import tables

def main():
    while True:
        response = raw_input("Say something: ")
        if not response:
            break
        words = response.split()
        tables.PrintTable(words)

if __name__ == '__main__':
    main() 
