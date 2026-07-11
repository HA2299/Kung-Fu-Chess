from piece import Piece


class Knight(Piece):

    def is_valid_pattern(self, start, end):
        row_diff = abs(start.row - end.row)
        col_diff = abs(start.col - end.col)

        return (
            (row_diff == 2 and col_diff == 1) or
            (row_diff == 1 and col_diff == 2)
        )