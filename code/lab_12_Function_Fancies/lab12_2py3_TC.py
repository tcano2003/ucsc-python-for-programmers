#!/usr/bin/env python3
"""
lab12_2.py
Write a function that receives a dictionary as an argument,
and returns a tuple of two formatted strings.
"""

def FormatEvent(event_d):
    calendar = "%(date)s:%(theme)s %(what)s" % event_d # '% event_d calls the dictionary'
    invitation = "Come to a %(theme)s %(what)s on %(date)s!" % event_d
    return (calendar, invitation)
    #can also "yield calendar; yield invitation
def main():
    event_d = {"what": "party", "date": "Oct 31", "theme": "Halloween"}
    for each in FormatEvent(event_d):
        print(each)

if __name__== '__main__':
    main()
