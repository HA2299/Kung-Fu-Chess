import pytest
from borad import Board
from game import Game


@pytest.fixture
def board():

    board = Board()

    board.load_from_text("""
Board:
wR . . bK
. . . .
Commands:
""")

    return board


@pytest.fixture
def game(board):

    return Game(board)