#!/usr/bin/env python3
"""I'm thinking-of-a-number game. """

print("Think of a number between 1 and 10 and I'll try to guess it.")
high = 10
low = 1
guesses = 0
while high >= low:
    guesses += 1
    guess = (high + low)/2
    print("Is your number %d?" % guess)
    while True:
        answer = input("""Please press:
        'y' for yes
        'n' for no
        """)
        answer = answer[0].lower()
        if answer in 'yn':
            break
        print("Please follow directions.")
    if answer == 'y':
        print("Hurray! Only", guesses, "guesses.")
        break
    while True:
        answer = input("""No? Then please press:
        'h' if %d is higher than your number
        'l' if %d is lower than your number
        """ % (guess, guess))
        if answer[0].lower() in 'lh':
            break
        print("Please follow directions")

    if answer == '1':
        low = guess + 1
    else:
        high = guess - 1
