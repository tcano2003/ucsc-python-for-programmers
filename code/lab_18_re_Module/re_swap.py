#!/usr/bin/env python
"""Swapping cats and dogs again, but this time doing a good
job with regular expressions.
"""
import re 

def DoSwap(text, apple, orange):
    """Swaps all occurances of apple for orange, and orange
    for apple in the text."""
    # Using VERBOSE and named groups for readability
    compiled_re = re.compile(r"""
    \b                 # word boundary
    (?P<found>%s|%s)   # apple or orange and puts the match
                       # in a group named "found" if the
                       # whole thing matches
    (?P<plural>s?)\b   # word boundary or 's' and a word 
                       # boundary and puts the 's', or not,
                       # into a group named "plural"
    """ % (re.escape(apple), re.escape(orange)),
           re.IGNORECASE | re.VERBOSE)

    def MatchCase(answer, like_string):
        if like_string.isupper():
            return answer.upper()
        if like_string.islower():
            return answer.lower()
        if like_string.istitle():
            return answer.title()
        return answer

    def SwapMatch(match_object):
        found = match_object.group("found")
        if found.lower() == apple.lower():
            found_cased = MatchCase(orange, found)
        else:
            found_cased =  MatchCase(apple, found) 
        return found_cased + match_object.group("plural")
    
    fixed = compiled_re.sub(SwapMatch, text)
    return fixed

def main():
    print DoSwap("ELEPHANTS: 14elephants are a lot of Dogs.",
                 "dog", "elephant")
    print DoSwap("3 Categories of CATS and dogs.", "cat","dog")

if __name__ == "__main__":
    main()
