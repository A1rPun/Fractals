#!/usr/bin/env python
from lsystem import LSystem

sierpinskiarrowhead = LSystem('A', 60, {
    'A': 'B-A-B', 
    'B': 'A+B+A',
})
sierpinskiarrowhead.iterate(4)
sierpinskiarrowhead.draw(10, 180)
