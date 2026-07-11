class MoveValidator:

    def is_valid_pattern(self, board, move):
        piece = board.get_piece(move.start)

        return piece.is_valid_pattern(move.start, move.end)