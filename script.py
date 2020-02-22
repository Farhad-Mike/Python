class Machine:
    __slots__ = ('x', 'y')
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


machine = Machine(2, 4)

machine.x = 5
