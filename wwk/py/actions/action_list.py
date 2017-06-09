#! /home/nsanthony/miniconda3/bin/python
from actions.jump import jump
from actions.attack import attack
from actions.die import die
from actions.nothing import nothing
from actions.run import run
from actions.look import look
from actions.move import move
from actions.hel import hell
from actions.attack_pc import attack_pc

action_list = {
        'nothing':nothing,'jump':jump,
        'attack':attack,'die':die,'run':run,
        'look':look,'move':move,'hell':hell,'attack_pc':attack_pc
}