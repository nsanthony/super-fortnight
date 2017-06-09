#! /home/nsanthony/miniconda3/bin/python
import people.people_class as p
from inventory.inventory_list import inventory_list
from weapons.weapon_list import weapon_list

person = p.people()
person.name = 'Prisoner'
person.health = 1
person.descript = 'A pathetic looking human'
person.weapon = weapon_list['unarmed']
person.armor = 0
person.hostile = 0

prisoner = person #change this to be the person that you want