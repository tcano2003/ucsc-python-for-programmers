#!/usr/bin/env python3
"""You can raise an exception anytime you take a notion."""
  
def GetPositiveNumber(prompt):
    """Writes the prompt to stdout and collects the response.
    Returns an int > 0 if one was given, ValueError otherwise.
    """
    said = input(prompt)
    number = float(said)
    if number > 0:
        return number
    raise ValueError ("Number given must be positive.")

if __name__ == '__main__':
    print (GetPositiveNumber("Positive number: "))

