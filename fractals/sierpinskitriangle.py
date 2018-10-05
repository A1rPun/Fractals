#!/usr/bin/env python
from lsystem import LSystem

sierpinskitriangle = LSystem('F-G-G', 120, {
    'F': 'F-G+F+G-F', 
    'G': 'GG',
})
sierpinskitriangle.iterate(4)
sierpinskitriangle.draw(10)
