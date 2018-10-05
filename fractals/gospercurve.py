#!/usr/bin/env python
from lsystem import LSystem

gosper = LSystem('A', 60, {
    'A': 'A-B--B+A++AA+B-', 
    'B': '+A-BB--B-A++A+B',
})
gosper.iterate(3)
gosper.draw(8)
