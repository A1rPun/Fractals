from math import sqrt

class Fractal(object):
    def __init__(self):
        self.name = ""


class LSystem(Fractal):
    def __init__(self, axiom='', angle=0, productions={}, ignore=''):
        self.lines = [axiom]
        self.angle = angle
        self.productions = productions
        self.ignore = ignore

    def iterate(self, n):
        if n >= len(self.lines):
            self.lines.append(''.join(self.productions.get(l, l) for l in self.lines[-1]))
            return self.iterate(n)
        else:
            return self.lines[n]


class Mandelbrot(Fractal):
    def __init__(self):
        self.MAX_ITER = 300
    
    def plot(self, x, y, width, height, zoom=1, moveX=0, moveY=0):
        preal = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
        pimag = (y - height / 2) / (0.5 * zoom * height) + moveY
        re = 0
        im = 0
        n = 0
        while re*re + im*im < 4 and n < self.MAX_ITER:
            re, im = re*re - im*im + preal, 2 * re*im + pimag
            n += 1
        return n


class Julia(Fractal):
    def __init__(self):
        self.MAX_ITER = 300
        self.cRe = -0.7
        self.cIm = 0.27015
    
    def plot(self, x, y, width, height, zoom=1, moveX=0, moveY=0):
        re = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
        im = (y - height / 2) / (0.5 * zoom * height) + moveY
        n = 0
        while re*re + im*im < 4 and n < self.MAX_ITER:
            re, im = re*re - im*im + self.cRe, 2 * re*im + self.cIm
            n += 1
        return n


class Goldenratio(Fractal):
    def __init__(self):
        self.phi = (1 + sqrt(5)) / 2
        self.angle = 90


fractals = [
    # Binary Tree
    LSystem('0', 45, {
        '0': '1[-0]+0', 
        '1': '11',
    }),
    # Cesaro
    LSystem('F', 85, { 'F': 'F+F--F+F' }),
    # Cross
    #LSystem('F--F--F', 90, 'F', { 'F': 'F+F--F+F' }),
    # Dragon Curve
    LSystem('FX', 90, {
        'X': 'X+YF+', 
        'Y': '-FX-Y',
    }),
    # Golden ratio
    Goldenratio(),
    # Gosper Curve    
    LSystem('A', 60, {
        'A': 'A-B--B+A++AA+B-', 
        'B': '+A-BB--B-A++A+B',
    }),
    # Hilbert Curve
    LSystem('A', 90, {
        'A': '-BF+AFA+FB-',
        'B': '+AF-BFB-FA+',
    }, 'AB'),
    # Julia set
    Julia(),
    # Koch Curve
    LSystem('F', 60, { 'F': 'F-F++F-F' }),
    # Koch Island
    LSystem('A-A-A-A', 90, { 'A': 'A-A+A+AA-A-A+A' }),
    # Koch Curve Quadratic
    LSystem('F', 90, { 'F': 'F+F-F-F+F' }),
    # Koch Snowflake
    LSystem('F++F++F', 60, { 'F': 'F-F++F-F' }),
    # Koch Triflake
    LSystem('F++F++F', 60, { 'F': 'F+F--F+F' }),
    # Levy C Curve
    LSystem('F+', 45, { 'F': '+F--F+' }),
    # Mandelbrot
    Mandelbrot(),
    # Mango Kolam
    LSystem('A---A', 60, {
        'A': 'f-F+Z+F-fA',
        'Z': 'F-FF-F--[--Z]F-FF-F--F-FF-F--',
    }, 'AZ'),
    # Mango Kolam 2
    LSystem('X', 60, {
        'X': '[-F+F[Y]+F][+F-F[X]-F]',
        'Y': '[-F+F[Y]+F][+F-F-F]',
    }, 'XY'),
    # Minkowski Sausage
    LSystem('F', 90, { 'F': 'F+F-F-FF+F+F-F' }),
    # Moore Curve
    LSystem('LFL+F+LFL', 90, {
        'L': '-RF+LFL+FR-',
        'R': '+LF-RFR-FL+',
    }, 'LR'),
    # Peano Curve
    LSystem('X', 90, {
        'X': 'XFYFX+F+YFXFY-F-XFYFX',
        'Y': 'YFXFY-F-XFYFX+F+YFXFY',
    }, 'XY'),
    # Penrose
    LSystem('[7]++[7]++[7]++[7]++[7]', 36, {
        '6': '81++91----71[-81----61]++', 
        '7': '+81--91[---61--71]+',
        '8': '-61++71[+++81++91]-',
        '9': '--81++++61[+91++++71]--71',
    }, '1'),
    # Pentaflake
    LSystem('F++F++F++F++F', 36, { 'F': 'F++F++F+++++F-F++F' }),
    # Pentigree Curve
    LSystem('F-F-F-F-F', 72, { 'F': 'F-F-F++F+F-F' }),
    # Plant
    LSystem('X', 25, {
        'X': 'F-[[X]+X]+F[+FX]-X', 
        'F': 'FF',
    }),
    # Sierpinski Arrowhead Curve
    LSystem('A', 60, {
        'A': 'B-A-B', 
        'B': 'A+B+A',
    }),
    # Sierpinski Carpet
    LSystem('F', 90,  {
        'F': 'F+F-F-F-G+F+F+F-F',
        'G': 'GGG',
    }),
    # Sierpinski Curve
    LSystem('L--F--L--F', 45,  {
        'L': '+R-F-R+',
        'R': '-L+F+L-',
    }),
    # Sierpinski Hexagon
    LSystem('X', 60, {
        'X': 'X+X+X+X+X+X+y', 
        'y': 'yyy',
    }),
    # Sierpinski Triangle
    LSystem('F-G-G', 120, {
        'F': 'F-G+F+G-F', 
        'G': 'GG',
    }),
    # Star
    LSystem('F', 77, { 'F': 'F++F' }),
    # Tri Tree
    LSystem('0', 90, {
        '0': '1-[0]+[0]+0', 
        '1': '11',
    }),
    # Unknown 1
    LSystem('F', 120, { 'F': 'F+F-F' }),
    # Unknown 2
    LSystem('F-F-F-F', 90, {
        'F': 'F-B+FF-F-FF-FB-FF+B-FF+F+FF+FB+FFF', 
        'B': 'BBBBBB',
    }),
    # Unknown 3
    LSystem('F+F+F+F', 90, { 'F': 'FF+F++F+F' }),
    # Unknown 4
    LSystem('A-A-A-A', 90, { 'A': 'AA-A-A-A-AA' }),
    # Unknown 5
    LSystem('F-F-F-F', 90, { 'F': 'FF-F-F-F-F-F+F' }),
]
