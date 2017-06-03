#! /Users/nsanthony/miniconda3/bin/python
from rooms import room_list
from rooms.room_list import room_map

def visable(location,other=None):
    """Template function, needs definition"""
    vis = {}
    if other == None:
        for keys in room_map:
            other = room_map[keys]
            c1 = location.coord
            c2 = other.coord
            d = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
            if d <= 2 & d != 0:
                vis[other.name] = other
    return vis