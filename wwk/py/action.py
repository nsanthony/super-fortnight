#! /Users/nsanthony/miniconda3/bin/python
from actions import action_set
from error import error

actions = {
        'nothing':action_set.nothing,'jump':action_set.jump,
        'attack':action_set.attack,'die':action_set.die,'run':action_set.run,
        'look':action_set.look,'move':action_set.move,'hell':action_set.hell
}

def action(location):
    """Action funciton call to do an action, needs definition"""
    print('What would you like to do?')
    k = input()
    act = 1
    try:
        location = actions[k](location)
        if k == 'nothing':
            act = 0
    except:
        print('error is in action')
        error()
        action(location)
    return act, location

