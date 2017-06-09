#! /Users/nsanthony/miniconda3/bin/python
import rooms.room_class as rc
from people.people_list import people_list
from people.people_directory import skellington_1, skellington_2


blank = rc.room()
blank.name = 'another_stone_room'
blank.descript = 'This room is full of skellingtons!'
blank.size = ''
blank.occupied = 1
blank.people = [people_list['skellington_1'],people_list['skellington_2'],people_list['prisoner']]
blank.people[0].armor = 0
blank.coord = [0,0,0]
blank.seen = 1
blank.vis = {}
blank.been = 0

skellington_room = blank