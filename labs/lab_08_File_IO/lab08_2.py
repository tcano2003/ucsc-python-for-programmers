#!/usr/bin/env python
"""
lab08_2.py
Write a function that takes a file name and counts
how many times each word appears in the file.
"""
import sys
import lab06_6 as count_vowels

def CountVowelsInFile(file_name):
    """Returns the number of vowels in the file named.
    """
    vowel_count = 0
    file_obj = open(file_name)
    try:
        for line in file_obj:
            vowel_count += count_vowels.CountVowels(line)
    finally:
        file_obj.close()
    return vowel_count

def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = raw_input("File name: ")
    if not file_name:
        file_name = 'cats.txt'
    try:
        print "There are %d vowels in %s." % (
            CountVowelsInFile(file_name), file_name)
    except IOError, info:
        print >> sys.stderr, info
        sys.exit(1)

if __name__ == '__main__':
    main()

"""
$ lab08_2.py
File name: 
There are 96 vowels in cats.txt.
$ lab08_2.py
File name: cats.txt
There are 96 vowels in cats.txt.
$ lab08_2.py
File name: Bogus
[Errno 2] No such file or directory: 'Bogus'[much deleted]
"""

