#!/usr/bin/env python
from lsystem import LSystem

thuemorse = LSystem('0', productions = {
    '0': '01', 
    '1': '10',
})
print(thuemorse.iterate(4))
