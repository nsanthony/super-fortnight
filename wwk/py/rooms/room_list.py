#! /Users/nsanthony/miniconda3/bin/python

from rooms.room_directory.blank_room import blank
from rooms.room_directory.woods import woods
from rooms.room_directory.cottage import cottage
from rooms.room_directory.cottage_ext import cottage_ext
from rooms.room_directory.skellington_room import skellington_room
from rooms.room_directory.location_template import blank
from rooms.room_directory.stone_room import stone_room

room_map = {"woods":woods,"blank":blank,"cottage":cottage,
            "outside_cottage":cottage_ext,'another_stone_room':skellington_room,
            'template':blank,'stone_room':stone_room,'skellington_room':skellington_room
        }

