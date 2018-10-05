#!/usr/bin/env python
from lsystem import LSystem

star = LSystem('F', 77, { 'F': 'F++F' })
star.iterate(7)
star.draw(200)
