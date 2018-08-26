#!/usr/bin/env python3
"""Provides CountVowels, a vowel counting function."""
import sys
import lab06_6py3 as count_vowels

def CountVowelsInFile(file_name):
    """Returns the number of vowels in a file
    """
    vowel_count = 0
    open_file = open(file_name)
    try:
        for line in open_file:
            vowel_count += count_vowels.CountVowels(line)
    finally:
        open_file.close()
    return vowel_count

def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = input("File name: ")
    if not file_name:
        file_name = 'cats.txt'
    try:
        print ("There are %d vowels in %s." % (
            CountVowelsInFile(file_name), file_name))
    except IOError as e:#, info:
        pass
        print >> sys.stderr, info
        sys.exit(1)
    
if __name__ == "__main__":
    main()
