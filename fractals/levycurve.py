#!/usr/bin/env python
from lsystem import LSystem

levycurve = LSystem('F+', 45, { 'F': '+F--F+' })
levycurve.iterate(8)
levycurve.draw(6)
