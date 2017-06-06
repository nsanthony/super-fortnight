#! /Users/nsanthony/miniconda3/bin/python
from people.people_list import people_list

def attack(location,option=None):
    """Used to attack, still needs definitions other than text out."""
    pc = people_list['pc']
    if option == None:
        print()
        print('You are able to attack:')
        for keys in location.people:
            print(location.people[keys].name)
        print()
        print('What would you like to attack?')
        k = input()
        for keys in people_list:
            if people_list[keys].name == k:
                opponent = people_list[keys]
    else:
        for keys in people_list:
            if people_list[keys].name == option:
                opponent = people_list[keys]
    damage = pc.weapon.damage
    print()
#    print('raw',damage)
    opp_dam_red = opponent.armor
#    print('damage reduction',opp_dam_red)
    dam_delt = damage - opp_dam_red
#    print('actual damage delt',dam_delt)
    if dam_delt <= 0:
        dam_delt = 0
        print('Weapon Ineffective')
    if opponent.health <= 0:
        dam_delt = 0
        print(opponent.name,'is already dead')
    else:
        opponent.health -= dam_delt
        print(opponent.name,'took',dam_delt,'damage')
        if opponent.health == 0:
            print(opponent.name,'died')
            
    return location