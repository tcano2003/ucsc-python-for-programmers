#!/usr/bin/env python
"""lab18_3.py This evil program crawls around on the web and 
collects email addresses. """

import sys, os, re, urllib, httplib

sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
import lab_12_Function_Fancies.timeout_decorator as time_out

EMAIL_CATCHER = re.compile(r"""
    [\s,:;(<\['\"]+([^@\s,;:\"]+)@
    ([^@\-\s,:;>\)'\"]+\.[a-z,A-Z]{2,3})[\s,;:\"'>\)]""")

URL_CATCHER = re.compile(r"""http://[^\s\"<>()']*\b""")

@time_out.TimeOut(3)
def CollectPage(url):
    try:
        urlpage = urllib.urlopen(url)
    except (IOError, httplib.InvalidURL):
        return None
    try:
        try:
            return urlpage.read()
        finally:
            urlpage.close()
    except:
        return None

def HarvestEmailAddresses(starting_url, max_pages=100):
    """Crawls through max_pages starting at starting_url
    and returns all the email addresses found.
    """
    pages_to_visit = [starting_url]
    addresses = []
    for page_no in range(max_pages):
        try:
            visiting_url = pages_to_visit[page_no]
        except IndexError:# ran out of pages before max_pages
            break
        ParsePage(visiting_url, addresses, pages_to_visit)
    return addresses




def ParsePage(url, addresses, pages_to_visit):
    """Updates addresses list with new addresses found
    and pages_to_visit list with new urls found.
    """
    try:
        text = CollectPage(url)
    except RuntimeError:
        return
    if text:
        for match in EMAIL_CATCHER.findall(text):
            address = '@'.join(match)
            if address not in addresses:
                addresses += [address]
        pages_to_visit += [url for url
                           in URL_CATCHER.findall(text)
                           if url not in pages_to_visit]

def main():
    starting_url = 'www.ngc.com'
    if len(sys.argv)>1:
        starting_url = sys.argv[1]
    if not starting_url.startswith('http://'):
        starting_url = 'http://' + starting_url
    print '\n'.join(HarvestEmailAddresses(starting_url, 100))

if __name__ == '__main__':
    main()
