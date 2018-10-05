#!/usr/bin/env python
from lsystem import LSystem

binarytree = LSystem('0', 45, {
    '0': '1[-0]+0', 
    '1': '11',
})
binarytree.iterate(6)
binarytree.draw(2, 270)
