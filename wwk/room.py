#! /Users/nsanthony/miniconda3/bin/python
from rooms import room_list
from error import error

rooms = {
        'blank':room_list.blank,'woods':room_list.woods,'cottage':room_list.cottage
        
}

def room(k):
    """This function calls one of the rooms"""
    current = room_list.blank
    try:
        current = rooms[k]
#        print('found room')
    except:
        error()
        
        
    return current