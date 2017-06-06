#! /Users/nsanthony/miniconda3/bin/python
import rooms.room_class as rc
from people.people_directory import person_template

blank = rc.room()
blank.name = 'blank room'
blank.descript = 'This is a blank room'
blank.size = 'You cant see the edge'
blank.occupied = 0
blank.people = person_template
blank.coord = [0,0,0]
blank.seen = 0
blank.vis = {}

name = blank