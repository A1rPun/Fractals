#!/usr/bin/env python
from lsystem import LSystem

sierpinskicarpet = LSystem('F', 90,  {
    'F': 'F+F-F-F-G+F+F+F-F',
    'G': 'GGG',
})
sierpinskicarpet.iterate(4)
sierpinskicarpet.draw(5, 45)
