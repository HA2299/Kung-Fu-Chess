from piece import Piece


class Bishop(Piece):

    def is_valid_pattern(self, start, end):
        return abs(start.row - end.row) == abs(start.col - end.col)

    @property
    def symbol(self):
        return self.color + "B"