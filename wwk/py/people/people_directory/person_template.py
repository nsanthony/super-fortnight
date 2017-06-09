#! /home/nsanthony/miniconda3/bin/python
import people.people_class as p
from inventory.inventory_list import inventory_list
from weapons.weapon_list import weapon_list

person = p.people()
person.name = ''
person.health = 0
person.descript = ''
person.weapon = weapon_list['unarmed']
person.armor = 0
person.hostile = 0

name_here = person #change this to be the person that you want