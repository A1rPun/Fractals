#!/usr/bin/env python
from lsystem import LSystem

cross = LSystem('F--F--F', 90, 'F', { 'F': 'F+F--F+F' })
cross.iterate(4)
cross.draw(8)
