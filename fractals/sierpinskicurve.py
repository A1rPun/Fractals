#!/usr/bin/env python
from lsystem import LSystem

sierpinskicurve = LSystem('L--F--L--F', 45,  {
    'L': '+R-F-R+',
    'R': '-L+F+L-',
})
sierpinskicurve.iterate(8)
sierpinskicurve.draw(4)
