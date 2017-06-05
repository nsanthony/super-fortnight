#! /Users/nsanthony/miniconda3/bin/python

from rooms.room_directory.blank_room import blank
from rooms.room_directory.woods import woods
from rooms.room_directory.cottage import cottage
from rooms.room_directory.cottage_ext import cottage_ext

room_map = {"woods":woods,"blank":blank,"cottage":cottage,
            "outside cottage":cottage_ext
        }

