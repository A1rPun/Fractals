#!/usr/bin/env python
from lsystem import LSystem

hilbert = LSystem('A', 90, {
    'A': '-BF+AFA+FB-',
    'B': '+AF-BFB-FA+',
}, 'AB')
hilbert.iterate(4)
hilbert.draw(4)
