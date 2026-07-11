from borad import Board
from command import Command
from game import Game


def test_print_board_command():

    board = Board()
    game = Game(board)

    command = Command(game)

    command.execute([
        "print board"
    ])