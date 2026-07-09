from constants import (
    BOARD_HEADER,
    COMMANDS_HEADER,
    ERROR_UNKNOWN_TOKEN,
    ERROR_ROW_WIDTH_MISMATCH,
    ERROR_MISSING_BOARD,
    VALID_TOKENS,
)
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

        try:
            start = lines.index(BOARD_HEADER) + 1
        except ValueError:
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
            self.board.append(tokens)

        self.rows = len(self.board)
        self.cols = expected_cols

    def _validate_tokens(self, tokens):
        for token in tokens:
            if not self._is_valid_token(token):
                raise ValueError(ERROR_UNKNOWN_TOKEN)

    def _is_valid_token(self, token):
        return token in VALID_TOKENS

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.board)