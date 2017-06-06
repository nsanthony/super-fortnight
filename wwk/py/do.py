#! /Users/nsanthony/miniconda3/bin/python
from action import action
from actions.action_list import action_list


def do(location,pc):
    """This function calls other functions when you want the pc to do soemthing
    for instance it calls action to get him to do one of the specified acitons
    until the pc is ready to move on and does nothing"""
    act = 1
    while act != 0:
        [act,location] = action(location)
        if location.people != None:
            for i in range(0,len(location.people)):
                person = location.people[i]
                if person.health > 0 & person.hostile == 1:
                    print()
                    pc = action_list['attack_pc'](person,pc)
            
    print()
    
    return location,pc