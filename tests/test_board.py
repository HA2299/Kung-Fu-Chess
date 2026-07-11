import pytest
from borad import Board
from king import King
from rook import Rook


def test_parse_valid_board():
    board = Board()

    text = """Board:
wK . . bK
. . . .
wR . . bR
Commands:
"""

    board.load_from_text(text)

    assert board.rows == 3
    assert board.cols == 4

    assert isinstance(
        board.board[0][0],
        King
    )

    assert board.board[0][1] is None

    assert isinstance(
        board.board[2][0],
        Rook
    )

def test_reject_unknown_token():
    board = Board()

    text = """Board:
wK xZ
. .
Commands:
"""

    with pytest.raises(ValueError, match="UNKNOWN_TOKEN"):
        board.load_from_text(text)


def test_reject_row_width_mismatch():
    board = Board()

    text = """Board:
wK . .
. bK
Commands:
"""

    with pytest.raises(ValueError, match="ROW_WIDTH_MISMATCH"):
        board.load_from_text(text)


def test_empty_board():
    board = Board()

    text = """Board:
Commands:
"""

    board.load_from_text(text)

    assert board.rows == 0
    assert board.cols == 0


def test_board_print_format():
    board = Board()

    text = """Board:
wK . bQ
. wN .
Commands:
"""

    board.load_from_text(text)

    assert str(board) == (
        "wK . bQ\n"
        ". wN ."
    )