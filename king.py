from piece import Piece


class King(Piece):

    def is_valid_pattern(self, start, end):
        row_diff = abs(start.row - end.row)
        col_diff = abs(start.col - end.col)

        return max(row_diff, col_diff) == 1

    @property
    def symbol(self):
        return self.color + "K"