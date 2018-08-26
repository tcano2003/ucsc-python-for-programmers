#!/usr/bin/env python3
"""You can override and extend the functionality."""
    
class NonPositiveNumber(ArithmeticError):
    
    times = 0
    
    def __init__(self, *args):
        "We call to the base class initializer and add some functionality."
        
        ArithmeticError.__init__(self, *args)
        NonPositiveNumber.times += 1

    def __str__(self):
        return "You messed %d %s! %s" % (
            NonPositiveNumber.times, "time" if
            NonPositiveNumber.times==1 else "times", self.args)

def GetPositiveNumber(prompt):
    """Writes the prompt to stdout and collects the response.
    Returns an int > 0 if one was given, raising:
      ValueError - if a number wasn't given
      NonPositiveNumber - if the number <= 0
         and giving back the non-positive number, if that was
         the problem.
    """
    said = input(prompt)
    number = float(said)
    if number > 0:
        return number
    raise NonPositiveNumber, ("Value not positive.", number)

def main():
    for trial in range(5):
        try:
            print (GetPositiveNumber("Number please: "))
        except NonPositiveNumber, exception_obj:
            print ("Caught NonPositiveNumber:", exception_obj)
        except ValueError, exception_obj:
            print ("Caught ValueError:", exception_obj)

if __name__ == '__main__':
    main()

