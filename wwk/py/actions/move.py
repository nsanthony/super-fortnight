#! /Users/nsanthony/miniconda3/bin/python
from rooms import room_list
from error import error
from room_finder import room_finder
from rooms.room_list import room_map
#==============================================================================
# rooms = {
#         'blank':room_list.blank,'woods':room_list.woods,'cottage':room_list.cottage
#         
# }
#==============================================================================

def move(location,option=None):
    """Move function. Use to move to new area, needs definition"""
    new_location = option
    if new_location != None:
        location = room_finder(new_location)
        print()
        print('You are now in',location.name)
        print(location.descript)
        print()
        location.been += 1
    else:
        print()
        print('you are in the',location.name)
        print()
        print('You can go to:')
        can_see = 0
        for keys in location.vis:
            if location.vis[keys].seen == 1:
                print(location.vis[keys].name)
                can_see += 1
        if can_see == 0:
            print('Nowhere')
        else:
            print('nowhere')
            print()
            print('Where would you like to go?')
            k = input()
            if k == 'nowhere':
                location = location
                print()
                print('You are now in',location.name)
                print()
                print(location.descript)
                print()
            else:
                location = room_finder(k) #this is used to call a room in a the room list
                print()
                print('You are now in',location.name)
                print(location.descript)
                print()
                location.been += 1
    return location