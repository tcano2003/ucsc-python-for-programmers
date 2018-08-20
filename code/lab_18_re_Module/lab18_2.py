#!/usr/bin/env python
"""lab18_2.py Swapping from a dictionary"""
import re

def DoReplace(text, replace_d):
    """Swaps all the replace_d.keys() in the text for
    their values."""
    # Using VERBOSE and named groups for readability
    compiled_re = re.compile(r"""
    \b                 # word boundary
    (?P<found>%s)      # matches any key and puts the match
                       # in a group named "found" 
    (?P<plural>s?)\b   # word boundary or 's' and a
                       # word boundary and puts the 's',
                       # or not, into a group named "plural"
    """ % ('|'.join([re.escape(k) for k in replace_d])),
                                  re.IGNORECASE | re.VERBOSE)

    def MatchCase(answer, cased_like_string):
        if cased_like_string.isupper():
            return answer.upper()
        if cased_like_string.islower():
            return answer.lower()
        if cased_like_string.istitle():
            return answer.title()
        return answer

    def SwapMatch(match_object):
        found = match_object.group('found')
        return MatchCase(replace_d[found.lower()], found)\
           + match_object.group('plural')
    
    fixed = compiled_re.sub(SwapMatch, text)
    return fixed

def main():
    replace_d = {
        'general':'band leader', 
        'china':'mexico', 
        'zen':'mariachi', 
        'master':'teacher', 
        'sword':'baton',
        'through':'around'}

    text = open('zen.story').read()
    print DoReplace(text, replace_d)

if __name__ == '__main__':
    main()
