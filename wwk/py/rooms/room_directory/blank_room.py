#! /Users/nsanthony/miniconda3/bin/python
import rooms.room_class as rc

blank = rc.room()
blank.name = 'blank room'
blank.descript = 'This is a blank room'
blank.size = 'You cant see the edge'
blank.occupied = 0
blank.people = 'There is no one in this room with you'
blank.coord = [0,0,0]