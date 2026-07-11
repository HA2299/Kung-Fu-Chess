from constants import (
    BOARD_HEADER,
    COMMANDS_HEADER,
    ERROR_UNKNOWN_TOKEN,
    ERROR_ROW_WIDTH_MISMATCH,
    ERROR_MISSING_BOARD,
    VALID_TOKENS,
)

from move import Move
from position import Position

from rook import Rook
from bishop import Bishop
from queen import Queen
from king import King
from knight import Knight


class Board:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.board = []

    def load_from_text(self, text):
        board_lines = self._extract_board_lines(text)
        self._parse_board(board_lines)

    def _extract_board_lines(self, text):
        lines = text.splitlines()

        start = None

        for i, line in enumerate(lines):
            if line.strip() == BOARD_HEADER:
                start = i + 1
                break

        if start is None:
            raise ValueError(ERROR_MISSING_BOARD)

        board_lines = []

        for line in lines[start:]:
            line = line.strip()

            if line == COMMANDS_HEADER:
                break

            if line:
                board_lines.append(line)

        return board_lines

    def _parse_board(self, board_lines):
        self.board = []

        if not board_lines:
            self.rows = 0
            self.cols = 0
            return

        expected_cols = None

        for row in board_lines:
            tokens = row.split()

            if expected_cols is None:
                expected_cols = len(tokens)
            elif len(tokens) != expected_cols:
                raise ValueError(ERROR_ROW_WIDTH_MISMATCH)

            self._validate_tokens(tokens)

            pieces_row = []

            for token in tokens:
                pieces_row.append(self._create_piece(token))

            self.board.append(pieces_row)

        self.rows = len(self.board)
        self.cols = expected_cols

    def _create_piece(self, token):

        if token == ".":
            return None

        color = token[0]
        piece_type = token[1]

        if piece_type == "R":
            return Rook(color)

        if piece_type == "B":
            return Bishop(color)

        if piece_type == "Q":
            return Queen(color)

        if piece_type == "K":
            return King(color)

        if piece_type == "N":
            return Knight(color)

        raise ValueError(ERROR_UNKNOWN_TOKEN)

    def _validate_tokens(self, tokens):
        for token in tokens:
            if not self._is_valid_token(token):
                raise ValueError(ERROR_UNKNOWN_TOKEN)

    def _is_valid_token(self, token):
        return token in VALID_TOKENS

    def __str__(self):
        result = []

        for row in self.board:
            result.append(
                " ".join(
                    "." if piece is None else piece.symbol
                    for piece in row
                )
            )

        return "\n".join(result)

    def is_inside(self, position: Position) -> bool:
        return (
            0 <= position.row < self.rows and
            0 <= position.col < self.cols
        )

    def get_piece(self, position: Position):
        return self.board[position.row][position.col]

    def set_piece(self, position: Position, piece):
        self.board[position.row][position.col] = piece

    def move_piece(self, move: Move):
        piece = self.get_piece(move.start)

        self.set_piece(move.end, piece)
        self.set_piece(move.start, None)