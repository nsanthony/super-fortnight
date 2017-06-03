#! /Users/nsanthony/miniconda3/bin/python
from rooms import room_list
from error import error
from visable import visable
from rooms.room_list import room_map
#rooms = {
#        'blank':room_list.blank,'woods':room_list.woods,'cottage':room_list.cottage
#        
#}

def room(k):
    """This function calls one of the rooms"""
    current = room_map['blank']
    try:
        current = room_map[k]
        vis = visable(location=current)
        current.vis = vis
#        print('found room')
    except:
        error()
        
        
    return current