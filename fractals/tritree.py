#!/usr/bin/env python
from lsystem import LSystem

triotree = LSystem('0', 90, {
    '0': '1-[0]+[0]+0', 
    '1': '11',
})
triotree.iterate(5)
triotree.draw(4, 270)
