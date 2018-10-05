#!/usr/bin/env python
from lsystem import LSystem

pentigree = LSystem('F-F-F-F-F', 72, { 'F': 'F-F-F++F+F-F' })
pentigree.iterate(3)
pentigree.draw(5)
