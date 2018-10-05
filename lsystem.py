from drawille import Turtle

class LSystem(object):
    def __init__(self, axiom='', angle=0, productions={}, ignore=''):
        super(LSystem, self).__init__()
        self.line = axiom
        self.axiom = axiom
        self.angle = angle
        self.productions = productions
        self.ignore = ignore

    def restore(self):
        self.line = self.axiom

    def iterate(self, n):
        if n == 0:
            return self.line
        else:
            self.line = ''.join(self.productions.get(c, c) for c in self.line)
            return self.iterate(n-1)

    def draw(self, size, initial_rotation=0):
        def restore():
            pos, angl = q.pop()
            t.up()
            t.move(pos[0], pos[1])
            t.rotation = angl
            t.down()

        def move(pen):
            if not pen: t.up()
            t.fd(size)
            if not pen: t.down()

        q = []
        methods = {
            '-': lambda: t.left(self.angle),
            '+': lambda: t.right(self.angle),
            '[': lambda: q.append(([t.pos_x, t.pos_y], t.rotation)),
            ']': restore,
        }
        for v in self.ignore:
            methods[v] = lambda: None

        t = Turtle()
        t.rotation = initial_rotation
        for c in self.line:
            try:
                methods[c]()
            except KeyError:
                move(c.isupper())
                pass

        print(t.frame())
