#! /home/nsanthony/miniconda3/bin/python
import people.people_class as p
from inventory.inventory_list import inventory_list
from weapons.weapon_list import weapon_list

person = p.people()
person.name = 'skellington_1'
person.health = 2
person.descript = 'This is a spooky scary skellington'
person.weapon = weapon_list['sword']
person.armor = 0
person.hostile = 1

skellington_1 = person #change this to be the person that you want