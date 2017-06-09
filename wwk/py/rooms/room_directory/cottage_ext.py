#! /Users/nsanthony/miniconda3/bin/python
import rooms.room_class as rc
from rooms.room_directory.cottage import cottage
blank = rc.room()
blank.name = 'outside_cottage'
blank.descript = 'This is the exterior of a small run down cottage. The lights to the cottage apear to be on however.'
blank.size = 'Medium'
blank.occupied = 0
blank.people = 'There is no one around the cottage'
blank.coord = [1,2,0]
blank.seen = 0

cottage_ext = blank