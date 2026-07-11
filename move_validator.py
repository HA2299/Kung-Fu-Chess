class MoveValidator:

    def is_valid(self, board, move):

        piece = board.get_piece(move.start)

        if piece is None:
            return False

        return piece.is_valid_pattern(
            move.start,
            move.end
        )