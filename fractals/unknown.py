#!/usr/bin/env python
from lsystem import LSystem


tetradragon = LSystem('F', 120, { 'F': 'F+F-F' })
tetradragon.iterate(5)
tetradragon.draw(10)


island = LSystem('F-F-F-F', 90, {
    'F': 'F-B+FF-F-FF-FB-FF+B-FF+F+FF+FB+FFF', 
    'B': 'BBBBBB',
})
island.iterate(2)
island.draw(2)


icy = LSystem('F+F+F+F', 90, { 'F': 'FF+F++F+F' })
icy.iterate(4)
icy.draw(2)


square = LSystem('A-A-A-A', 90, { 'A': 'AA-A-A-A-AA' })
square.iterate(4)
square.draw(2)


squarestar = LSystem('F-F-F-F', 90, { 'F': 'FF-F-F-F-F-F+F' })
squarestar.iterate(3)
squarestar.draw(4)
