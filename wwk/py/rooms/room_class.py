#! /Users/nsanthony/miniconda3/bin/python
from people.people_list import people_list
import people.people_class as pe
class room:
    """This is a room class with atributes...."""
    def name():
        n = 'room name here'
        return n
    def descript():
        d = 'description here'
        return d
    def size():
        s = 'size here'
        return s
    def occupied():
        o = 0
        return o
    def people():
        p = [pe.people()]
        return p
    def coord():
        """This descripbes the coordinates of the room"""
        c = [0,0,0]
        return c
    def seen():
        """This determines if you have seen the room or not. Default 0"""
        s = 0
        return s
    def vis():
        v = {}
        return v
    def been():
        b = 0
        return b