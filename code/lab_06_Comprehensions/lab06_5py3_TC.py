#!/usr/bin/env python3
"""
Defines function that displays colors, 4 on a line.
"""
def DisplayColors():
    colors = ["beige", "silver", "charcoal", "royal blue",
              "aquamarine", "forest green", "chartreuse",
              "lime", "golden", "goldenrod", "coral", "salmon",
              "hot pink", "fuchsia", "lavender", "plum",
              "indigo", "maroon", "crimson", "lemon"]
    for i, color in enumerate(sorted(colors)): #sort and enumerate so that have index of each one
    #for i, color in enumerate(sorted(colors), key=lambda c:c[-1]): #sorts by last letter??
        print ("%15s" % color, end='')
        if i % 4 == 3: #every fourth time, create new line
        if i % 4 == 3:
            print()
def main():
    DisplayColors()

if __name__ == "__main__":
    main()
