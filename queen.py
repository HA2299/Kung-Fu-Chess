from piece import Piece


class Queen(Piece):

    def is_valid_pattern(self, start, end):
        row_diff = abs(start.row - end.row)
        col_diff = abs(start.col - end.col)

        return (
            start.row == end.row or
            start.col == end.col or
            row_diff == col_diff
        )