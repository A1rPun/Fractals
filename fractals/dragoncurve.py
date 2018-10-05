#!/usr/bin/env python
from lsystem import LSystem

dragon = LSystem('FX', 90, {
    'X': 'X+YF+', 
    'Y': '-FX-Y',
})
dragon.iterate(10)
dragon.draw(2, 90)
