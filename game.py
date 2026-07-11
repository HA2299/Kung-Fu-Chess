from move import Move
from move_validator import MoveValidator

class Game:

    def __init__(self, board):
        self.board = board
        self.selected_position = None
        self.validator = MoveValidator()

    def click(self, position):

        if not self.board.is_inside(position):
            return

        token = self.board.get_piece(position)

        if self.selected_position is None:

            if token is not None:
                self.selected_position = position

            return

        move = Move(self.selected_position, position)

        if self.validator.is_valid(self.board, move):
            self.board.move_piece(move)

        self.selected_position = None