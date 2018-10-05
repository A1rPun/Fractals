#!/usr/bin/env python
from lsystem import LSystem

kochsnowflake = LSystem('F++F++F', 60, { 'F': 'F-F++F-F' })
kochsnowflake.iterate(4)
kochsnowflake.draw(2)
