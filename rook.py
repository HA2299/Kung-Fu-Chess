from piece import Piece


class Rook(Piece):

    def is_valid_pattern(self, start, end):
        return (
            start.row == end.row or
            start.col == end.col
        )