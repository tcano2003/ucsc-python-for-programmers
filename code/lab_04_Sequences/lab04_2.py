#!/usr/bin/env python
""" Ask the user for exactly 5 words, one at a time. After
each word is collected from the user, print it only if it
is not a duplicate of a word already collected.
"""

def AskForAndPrintUniqueWords(number_of_words):
    words = []
    for loop in range(number_of_words):
        new_word = raw_input("Word please: ")
        if not new_word:
            break
        if not new_word in words:
            print new_word
            words += [new_word]

def main():
    AskForAndPrintUniqueWords(5)
main()

