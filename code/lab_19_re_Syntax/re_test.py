#!/usr/bin/env python
"""This exercise is from the book "Perl by Example" by
Ellie Quigley.  The exercise in Ellie's book asks us to
print the city and state where Norma lives.

I used this little program to develop the regular
expression."""

import re, sys  

def ReTest(re_str, data, flags):
    """Test the re_str against the data with flags.

    If it doesn't find a hit, try again with one character
    trimmed off the end, and again, and again, until a hit
    is found.  Then give a report.
    """
    len_re_str = len(re_str)
    for index in range(len_re_str, 0, -1):
        try:
            m = re.search(re_str[:index], data, flags)
        except: # many sre_contants.errors
            continue
        if m != None:
            break
    else:
        print "None of it worked!"
        return

    if index == len_re_str:
        print "It worked!"
        print "Groups:", m.groups()
        return
    
    print "This much worked:"
    print re_str[:index]
    print "Groups:", m.groups()
    print "It broke here:"
    print re_str[index:]

def main():        
    re_str = r"""
    ^%s      # Line starts with the name
    \b       # followed by a non-word character
    (?:      # Un-captured group with anything
    [^:]+    # except colons,  followed by a
    :){2}    # colon. That group twice.
    x        # a mistake!!!
    [^,]+    # All characters up to a comma,
    ,[ ]+    # a comma and some spaces. 
    (?P<town># Capturing a group and naming it "town". 
    [^\d]+)  # with anything but digits
    \d       # a digit ends the match
    """ % 'Norma'
    data = """
Tommy Savage:408-724-0140:1222 Oxbow Court, Sunnyvale, CA 94087:5/19/66:34200
Betty Boop:245-836-2837:6937 Ware Road, Milton, PA 93756:9/21/46:43500
Wilhelm Kopf:846-836-2837:6937 Ware Road, Milton, PA 93756:9/21/46:43500
Norma Corder:397-857-2735:74 Pine Street, Dearborn, MI 23874:3/28/45:245700
James Ikeda:834-938-8376:23445 Aster Ave., Allentown, NJ 83745:12/1/38:45000
Barbara Kerz:385-573-8326:832 Pnce Drive, Gary, IN 83756:12/15/46:26850
"""
    ReTest(re_str, data, re.VERBOSE + re.MULTILINE)

if __name__ == '__main__':
    main()
