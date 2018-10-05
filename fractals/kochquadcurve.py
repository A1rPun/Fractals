#!/usr/bin/env python
from lsystem import LSystem

koch = LSystem('F', 90, { 'F': 'F+F-F-F+F' })
koch.iterate(4)
koch.draw(2, 180)
