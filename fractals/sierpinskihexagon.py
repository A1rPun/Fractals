#!/usr/bin/env python
from lsystem import LSystem

sierpinskitriangle = LSystem('X', 60, {
    'X': 'X+X+X+X+X+X+y', 
    'y': 'yyy',
})
sierpinskitriangle.iterate(5)
sierpinskitriangle.draw(4)
