#! /Users/nsanthony/miniconda3/bin/python
from rooms import room_list
from rooms.room_list import room_map

def visable(location,other=None):
    """Template function, needs definition"""
    vis = {}
    if other == None:
        c1 = location.coord
        if c1[2] < 0:
            for keys in room_map:
                other = room_map[keys]
                c2 = other.coord
                d = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
                if d == 0:
                    vis = {}
                    vis[other.name] = other
        else:
            for keys in room_map:
                other = room_map[keys]
                c2 = other.coord
                d = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
                if d == 0 & c1[2] != c2[2]:
                    other.seen = 1
                    vis[other.name] = other
                elif d <= 2 & d > 0:
                    vis[other.name] = other
        return vis
    elif other != None:
        c1 = location.coord
        c2 = other.coord
        d = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
        if d <= 2:
            vis = 1
        else:
            vis = 0
        return vis