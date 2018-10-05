#!/usr/bin/env python
from lsystem import LSystem

peano = LSystem('X', 90, {
    'X': 'XFYFX+F+YFXFY-F-XFYFX',
    'Y': 'YFXFY-F-XFYFX+F+YFXFY',
}, 'XY')
peano.iterate(3)
peano.draw(4, 90)
