from position import Position
from rook import Rook
from bishop import Bishop
from knight import Knight
class MoveValidator:

    def is_valid(self, board, move):

        piece = board.get_piece(move.start)

        if piece is None:
            return False

        if not piece.is_valid_pattern(move.start,move.end):
            return False
        
        if not self._is_path_valid(board, piece, move):
            return False
        
        if not self._is_capture_valid(board,piece,move):
            return False
        
        return True
        
        


    def _is_path_valid(self, board, piece, move):

        if isinstance(piece, Knight):
            return True

        if isinstance(piece, (Rook, Bishop)):
            return self._path_is_clear(board, move)

        return True
    
    def _path_is_clear(self, board, move):

        row_step = 0
        col_step = 0

        if move.end.row > move.start.row:
            row_step = 1
        elif move.end.row < move.start.row:
            row_step = -1

        if move.end.col > move.start.col:
            col_step = 1
        elif move.end.col < move.start.col:
            col_step = -1

        row = move.start.row + row_step
        col = move.start.col + col_step

        while (row, col) != (move.end.row, move.end.col):

            if board.get_piece(Position(row, col)) is not None:
                return False

            row += row_step
            col += col_step

        return True

    def _is_capture_valid(self, board, piece, move):

        target = board.get_piece(move.end)

        if target is None:
            return True

        return piece.color != target.color