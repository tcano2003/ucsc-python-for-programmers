#!/usr/bin/env python3
"""You can invent your own exception, having it inherit from 
some class in the Exception hierarchy."""
    
class NonPositiveNumber(ArithmeticError):
    """Defines a new exception class with the same behavior
    as any builtin ArithmeticError."""
    pass

def GetPositiveNumber(prompt):
    """Writes the prompt to stdout and collects the response.
    Returns an int > 0 if one was given, raising:
      ValueError - if a number wasn't given
      NonPositiveNumber - if the number <= 0
         and reporting the non-positive number, if that was
         the problem.
    """
    said = input(prompt)
    number = float(said)
    if number > 0:
        return number
    raise NonPositiveNumber, ("Number given must be positive.", number)
def main():
    for trial in range(3):
        try:
            print (GetPositiveNumber("Number please: "))
        except NonPositiveNumber, exception_obj:
            print ("Caught NonPositiveNumber:", exception_obj)
        except ValueError, exception_obj:
            print ("Caught ValueError:", exception_obj)

if __name__ == '__main__':
    main()
