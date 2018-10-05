#!/usr/bin/env python
from lsystem import LSystem

minkowski = LSystem('F', 90, { 'F': 'F+F-F-FF+F+F-F' })
minkowski.iterate(3)
minkowski.draw(4)
