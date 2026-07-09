from borad import Board
from commands import Command


def test_print_board_command(capsys):

    board = Board()

    text = """Board:
wK . .
. bK .
Commands:
"""

    board.load_from_text(text)

    command = Command(board)

    command.execute([
        "print board"
    ])

    captured = capsys.readouterr()

    assert captured.out == (
        "wK . .\n"
        ". bK .\n"
    )