#!/usr/bin/env python
"""Interactive vowel counter."""

import lab05_1
import sys

def main():
    while True:
        sys.stdout.write("Phrase: ")
        count_this = sys.stdin.readline()
        if count_this == '\n':
            break
        sys.stdout.write("... has %d vowels.\n" % (
            lab05_1.CountVowels(count_this)))

if __name__ == '__main__':
    main()

