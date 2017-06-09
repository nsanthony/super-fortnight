#! /home/nsanthony/miniconda3/bin/python
import people.people_class as p
from inventory.inventory_list import inventory_list
from weapons.weapon_list import weapon_list

person = p.people()
person.health = 10
person.descript = 'You are the pc, use your imagination'
person.weapon = weapon_list['unarmed']
person.armor = 0

pc = person