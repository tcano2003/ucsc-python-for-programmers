#!/usr/bin/env python3
"""Provides CountVowels, a vowel counting function.
"""

def TestforVowels(sentence):
    vowel_count = 0
    for char in sentence:
        if char in 'aeiouAEIOU':
            vowel_count = vowel_count + 1 # vowel_count += 1
    #return vowel_count
    print(vowel_count)

def main():
    sentence = "Math, science, history, unraveling the mysteries, that all started with the big bang!"
    TestforVowels(sentence)
    #print(vowel_count)

if __name__ == '__main__':
    main()
