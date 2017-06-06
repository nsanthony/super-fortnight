#! /Users/nsanthony/miniconda3/bin/python


def look(location,option=None):
    """Look around, needs definition"""
    print()
    print(location.descript)
    occupied_count = 0
    if location.people != None:
        for i in range(0,len(location.people)): #chekcs for living creatures
            person = location.people[i]
            if person.health > 0:
                occupied_count += 1
        if occupied_count > 0: #prints out the names of living creatures in here
            print('In',location.name,'you find:')
            for i in range(0,len(location.people)):
                if person.health > 0:
                    person = location.people[i]
                    print(person.name)
    print()
    print("From here you can see:")
    can_see = 0
    for keys in location.vis:
        if location.vis[keys].seen == 1:
            print(location.vis[keys].name)
            can_see += 1
    if can_see == 0:
        print('Nothing else but you current surroundings')
    return location