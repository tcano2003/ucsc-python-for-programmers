#!/usr/bin/env python
"""
lab12_2.py
Write a function that receives a dictionary as an argument,
and returns a tuple of two formatted strings.
"""

def FormatEvent(event_d):
    """Returns two strings for the event:
    one formatted for a calendar,
    one formatted for an invitation.
    """
    calendar = "%(date)s:%(theme)s %(what)s" % event_d
    invitation = "Come to a %(theme)s %(what)s on %(date)s!" \
      % event_d
    return (calendar, invitation)

def main():
    event_d = {"what": "party", "date": "Oct 31",
               "theme": "Halloween"}
    for each in FormatEvent(event_d):
        print each

if __name__ == '__main__':
    main()

