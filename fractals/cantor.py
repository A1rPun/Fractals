#!/usr/bin/env python
from lsystem import LSystem

cantor = LSystem('A', productions = {
    'A': 'ABA', 
    'B': 'BBB',
})
print(cantor.iterate(4))
