#!/usr/bin/env python
from lsystem import LSystem

island = LSystem('A-A-A-A', 90, { 'A': 'A-A+A+AA-A-A+A' })
island.iterate(3)
island.draw(2)
