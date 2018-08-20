#!/usr/bin/env python
"""lab19_5.py Print all lines that don't contain "Boop"."""
import re
import norma  # to collect the data

def GetNotName(name, text):
    return re.findall(
        r"""^    # at the beginning of a line
        (?!      # must not match
        .*%s.*)  # the name anywhere
        (.*)     # but do match the whole line
        $        # to the end
        """ % name, text, re.MULTILINE|re.VERBOSE)

def main():
    print '\n'.join(GetNotName('Boop',
                               norma.ReadFile('address.data')))

if __name__ == '__main__':
    main()

