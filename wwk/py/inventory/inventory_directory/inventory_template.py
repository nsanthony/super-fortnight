#! /home/nsanthony/bin/python
import inventory.inventory_class as inv
from weapons.weapon_list import weapon_list


empty = inv.inventory()
empty.weapon =  weapon_list['stick']

empty = empty #put inventory name here 

