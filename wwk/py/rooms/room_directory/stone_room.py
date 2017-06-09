#! /Users/nsanthony/miniconda3/bin/python
import rooms.room_class as rc
from people.people_directory import person_template

blank = rc.room()
blank.name = 'stone_room'
blank.descript = 'This is a large stone room with a single door at the other end.'
blank.size = ''
blank.occupied = 0
blank.people = None
blank.coord = [1,1,0]
blank.seen = 1
blank.vis = {}
blank.been = 0

stone_room = blank