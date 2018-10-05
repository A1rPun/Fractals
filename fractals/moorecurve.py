#!/usr/bin/env python
from lsystem import LSystem

moorecurve = LSystem('LFL+F+LFL', 90, {
    'L': '-RF+LFL+FR-',
    'R': '+LF-RFR-FL+',
}, 'LR')
moorecurve.iterate(3)
moorecurve.draw(4)
