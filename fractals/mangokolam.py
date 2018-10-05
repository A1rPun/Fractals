#!/usr/bin/env python
from lsystem import LSystem

mangokolam = LSystem('A---A', 60, {
    'A': 'f-F+Z+F-fA',
    'Z': 'F-FF-F--[--Z]F-FF-F--F-FF-F--',
}, 'AZ')
mangokolam.iterate(6)
mangokolam.draw(6, 90)

mangokolamhex = LSystem('X', 60, {
    'X': '[-F+F[Y]+F][+F-F[X]-F]',
    'Y': '[-F+F[Y]+F][+F-F-F]',
}, 'XY')
mangokolamhex.iterate(8)
mangokolamhex.draw(10, 90)
