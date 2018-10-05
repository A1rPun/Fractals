#!/usr/bin/env python
from lsystem import LSystem

binarytree = LSystem('[7]++[7]++[7]++[7]++[7]', 36, {
    '6': '81++91----71[-81----61]++', 
    '7': '+81--91[---61--71]+',
    '8': '-61++71[+++81++91]-',
    '9': '--81++++61[+91++++71]--71',
}, '1')
binarytree.iterate(5)
binarytree.draw(4, 270)
