#!/usr/bin/env python
from lsystem import LSystem

plant = LSystem('X', 25, {
    'X': 'F-[[X]+X]+F[+FX]-X', 
    'F': 'FF',
})
plant.iterate(4)
plant.draw(4, 270)
