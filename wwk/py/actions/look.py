#! /Users/nsanthony/miniconda3/bin/python


def look(location):
    """Look around, needs definition"""
    print()
    print(location.descript)
    print(location.people)
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