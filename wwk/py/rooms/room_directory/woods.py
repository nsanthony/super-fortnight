#! /Users/nsanthony/miniconda3/bin/python
from rooms import room_class as rc

woods = rc.room()
woods.name = 'Woods'
woods.descript = 'You are alone in the woods'
woods.size =  'large'
woods.occupied = 1
woods.people = {}
woods.coord = [0,1,0]
woods.seen = 1