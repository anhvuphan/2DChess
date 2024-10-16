class Move:

    def __init__(self, initial, final, captured_piece=None):
        # initial and final are squares
        self.initial = initial
        self.final = final
        self.captured_piece = captured_piece  # quân cờ bị bắt (nếu có)

    def __str__(self):
        s = ''
        s += f'({self.initial.col}, {self.initial.row})'
        s += f' -> ({self.final.col}, {self.final.row})'
        return s

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final