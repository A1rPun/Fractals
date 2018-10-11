#!/usr/bin/env python
import curses
import time
from math import pi
from drawille import Canvas, Turtle, getTerminalSize
from fractals import LSystem, Mandelbrot, Julia, Goldenratio, fractals


def lsystem2drawille(lsystem, n, size, initial_rotation):
    def restore():
        pos, angl = q.pop()
        t.up()
        t.move(pos[0], pos[1])
        t.rotation = angl
        t.down()

    def move(pen):
        if not pen:
            t.up()
        t.fd(size)
        if not pen:
            t.down()

    q = []
    methods = {
        '-': lambda: t.left(lsystem.angle),
        '+': lambda: t.right(lsystem.angle),
        '[': lambda: q.append(([t.pos_x, t.pos_y], t.rotation)),
        ']': restore,
    }
    for v in lsystem.ignore:
        methods[v] = lambda: None
    t = Turtle()
    t.rotation = initial_rotation
    for c in lsystem.iterate(n):
        try:
            methods[c]()
        except KeyError:
            move(c.isupper())
            pass
    return t.frame()


def mandelbrot2drawille(mandelbrot, n):
    can = Canvas()
    w, h = getTerminalSize()
    w *= 2
    h *= 4
    for row in range(h):
        for col in range(w):
            if mandelbrot.plot(col, row, w, h, n) >= mandelbrot.MAX_ITER:
                can.set(col, row)
    return can.frame()


def julia2drawille(julia, n):
    can = Canvas()
    w, h = getTerminalSize()
    w *= 2
    h *= 4
    for row in range(h):
        for col in range(w):
            if julia.plot(col, row, w, h, n) >= julia.MAX_ITER:
                can.set(col, row)
    return can.frame()


def goldenratio2drawille(goldenratio, n, s, angle):
    def square(size):
        for i in range(4):
            t.forward(size)
            t.right(goldenratio.angle)
    
    def circle(radius, extent = 360, step = 360):
        sideLength = (2 * pi * radius) / step
        turnAngle = extent / step
        for i in range(step):
            t.forward(sideLength)
            t.right(turnAngle)

    t = Turtle()
    size = getTerminalSize()[0] + s
    t.rotation = goldenratio.angle + angle
    
    for i in range(n):
        square(size)
        t.forward(size)
        t.right(goldenratio.angle)
        t.forward(size)
        size /= goldenratio.phi
        
    t.up()
    t.move(0, 0)
    t.down()
    size = getTerminalSize()[0] + s
    t.rotation = goldenratio.angle + angle

    for i in range(n):
        circle(size / 4, 90)
        size /= goldenratio.phi

    return t.frame()

def getDrawing():
    global currentfractal, drawing, iteration, size, angle
    fractal = fractals[currentfractal]
    if isinstance(fractal, Mandelbrot):
        drawing = mandelbrot2drawille(fractal, iteration)
    elif isinstance(fractal, Julia):
        drawing = julia2drawille(fractal, iteration)
    elif isinstance(fractal, Goldenratio):
        drawing = goldenratio2drawille(fractal, iteration, size, angle)
    else:
        drawing = lsystem2drawille(fractal, iteration, size, angle)
    # Restrict viewport because curses can't handle UTF outside viewport
    termSize = getTerminalSize()
    drawing = '\n'.join(map(lambda x: x[:termSize[0] - 1], drawing.split('\n')[:termSize[1] - 1]))


def movefractal(left=False):
    global currentfractal, iteration, size, angle
    currentfractal += -1 if left else 1
    if currentfractal < 0:
        currentfractal = len(fractals) - 1
    elif currentfractal >= len(fractals):
        currentfractal = 0
    iteration = 1
    size = 10
    angle = 0


def main(stdscr):
    global drawing, iteration, size, angle

    def restore():
        getDrawing()
        stdscr.clear()

    while True:
        stdscr.addstr(0, 0, drawing)
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('s'):
            size += 1
            restore()
        elif key == ord('a'):
            if size > 1:
                size -= 1
                restore()
        elif key == ord('z'):
            angle = 360 if angle <= 1 else angle - 45           
            restore()
        elif key == ord('x'):
            angle = 0 if angle >= 359 else angle + 45
            restore()
        elif key == curses.KEY_LEFT:
            movefractal(True)
            restore()
        elif key == curses.KEY_RIGHT:
            movefractal()
            restore()
        elif key == curses.KEY_UP:
            iteration += 1
            restore()
        elif key == curses.KEY_DOWN:
            if iteration > 1:
                iteration -= 1
                restore()
        else:
            time.sleep(1)


drawing = ""
currentfractal = 0
iteration = 1
size = 10
angle = 0
getDrawing()

if __name__ == '__main__':
    curses.wrapper(main)
    print(drawing)
