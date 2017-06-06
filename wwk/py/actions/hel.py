#! /Users/nsanthony/miniconda3/bin/python
from actions import action_set

def hell(location,option=None):
    """This prints all of the possible commands, needs definition"""
    action = {
        'nothing':action_set.nothing,'jump':action_set.jump,
        'attack':action_set.attack,'die':action_set.die,'run':action_set.run,
        'look':action_set.look,'move':action_set.move
    }
    print()
    print('You can take these actions:')
    for keys, value in action.items():
        print(keys)
    print()
    return location