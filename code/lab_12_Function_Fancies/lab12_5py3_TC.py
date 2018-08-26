#! /usr/bin/env python3
"""
Testing dice.py by reading it as a text file, making a little
change, and then executing it, via the exec command.
"""
import sys, os

def GetDiceCodeString():
    """Read the dice.py file as text and change random.randrange
    to be doubles_generator_object.next(), and return the text.
    """
    file_path = os.path.join('..', 'lab_03_Functions', 'dice.py')
    dice_code = open(file_path).read()
    dice_code = dice_code.replace(
        "random.randrange(1, 7)",
        "doubles_generator_object.next()")
    # The __name__ is '__main__' so the code will run when
    # exec-ed.  Stopping that:
    end_at = dice_code.find("def main")
    dice_code = dice_code[:end_at]
    return dice_code

def RollDeterminedDice():
    """Returns a roll of the dice, in order so that doubles
    are rolled.
    """
    for die in range(1,7): #have determined dice
        yield die
        yield die

def TestRollem():
    """Tests the Rollem function in dice.py.
    """
    global doubles_generator_object #making global so can be foudn
    # doubles_generator_object needs to be in the global 
    # space for Rollem() to find it.
    
    dice_code = GetDiceCodeString()

    doubles_generator_object = RollDeterminedDice()

    exec (dice_code)
    for roll in range(6):
        print (Rollem())
    
TestRollem()
