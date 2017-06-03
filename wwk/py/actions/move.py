#! /Users/nsanthony/miniconda3/bin/python
from rooms import room_list
from error import error
from room import room
from rooms.room_list import room_map
#==============================================================================
# rooms = {
#         'blank':room_list.blank,'woods':room_list.woods,'cottage':room_list.cottage
#         
# }
#==============================================================================

def move(location):
    """Move function. Use to move to new area, needs definition"""
    print()
    print('you are in the',location.name)
    print('You can go to:')
    for keys in location.vis:
        print(location.vis[keys].name)
    print('Where would you like to go?')
    k = input()
    location = room(k) #this is used to call a room in a the room list
    print()
    print('You are now in',location.name)
    print(location.descript)
    print()
    return location