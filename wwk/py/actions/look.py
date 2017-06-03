#! /Users/nsanthony/miniconda3/bin/python


def look(location):
    """Look around, needs definition"""
    print()
    print(location.descript)
    print(location.people)
    print("From here you can see:")
    for keys in location.vis:
        print(location.vis[keys].name)
    return location