#!/usr/bin/env python
"""lab11_2.py  (Optional)

Profiles four methods of accessing all the elements in
a sequence.
"""

def DoLens(sequence):
    i = 0
    while i < len(sequence):
        sequence[i]
        i += 1

def DoWhile(sequence):
    i = 0
    sequence_len = len(sequence)
    while i < sequence_len:
        sequence[i]
        i += 1

def DoRange(sequence):
    for i in range(len(sequence)):
        sequence[i]

def DoIterator(sequence):
    for element in sequence:
        element

def Profile(times=1):
    planets = ("Mercury", "Venus", "Earth", "Mars", 
               "Jupiter", "Saturn", "Uranus", "Neptune")
    for time in range(times):
        DoLens(planets)
        DoWhile(planets)
        DoRange(planets)
        DoIterator(planets)

def main():
    import cProfile
    cProfile.run("Profile(5000)")

main()

