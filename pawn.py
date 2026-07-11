from piece import Piece


class Pawn(Piece):

    def is_valid_pattern(self, start, end):
        raise NotImplementedError