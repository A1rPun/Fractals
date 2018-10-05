#!/usr/bin/env python
from lsystem import LSystem

binarytree = LSystem('F++F++F++F++F', 36, { 'F': 'F++F++F+++++F-F++F' })
binarytree.iterate(3)
binarytree.draw(6)
