#! /Users/nsanthony/miniconda3/bin/python
from people.people_list import people_list

def attack_pc(opponent,pc):
    """Template function, needs definition"""
    enemy = opponent
    damage = enemy.weapon.damage
    pc_dam_red = pc.armor
    dam = damage - pc_dam_red
    if dam <= 0:
        dam = 0
    pc.health -= dam
    print(opponent.name,'attacks you dealing,',dam,'damage')
    print('You are currently at',pc.health,'health')
    return pc