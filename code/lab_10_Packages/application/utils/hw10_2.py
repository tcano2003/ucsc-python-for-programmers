#!/usr/bin/env python
"""Provides Palindromize(phrase)"""

import string

def Palindromize(phrase):
    """Returns lowercase version of the phrase, which can be a
    number, or contain numbers, with whitespace and punctuation
    removed if the phrase is a palindrome.  If not, it returns
    None."""

    phrase = ''.join([c for c in str(phrase).lower() if c.isalnum()])
    if phrase == phrase[::-1]:
        return phrase
    return None

def main():
    DATA = ('Murder for a jar of red rum', 1.2321,
            'nope', 'abcbA', 3443, 'what',
            'Never odd or even', 'Rats live on no evil star')
    for phrase in DATA:
        answer = Palindromize(phrase)
        if answer:
            print "%s -> %s" % (phrase, answer)

if __name__ == '__main__':
    main()

"""
$ ;verbbf{hw10_2.py}
Murder for a jar of red rum -> murderforajarofredrum
1.2321 -> 12321
abcbA -> abcba
3443 -> 3443
Never odd or even -> neveroddoreven
Rats live on no evil star -> ratsliveonnoevilstar
$"""
