#!/usr/bin/env python
from lsystem import LSystem

cesaro = LSystem('F', 85, { 'F': 'F+F--F+F' })
cesaro.iterate(4)
cesaro.draw(10, 180)
