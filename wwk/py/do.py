#! /Users/nsanthony/miniconda3/bin/python
from action import action


def do(location):
    """This function calls other functions when you want the pc to do soemthing
    for instance it calls action to get him to do one of the specified acitons
    until the pc is ready to move on and does nothing"""
    act = 1
    while act != 0:
        [act,location] = action(location)
        print()
    
    return location