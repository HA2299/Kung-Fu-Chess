import sys

from borad import Board
from command import Command
from fixture_parser import extract_commands
from game import Game


def run():
    text = sys.stdin.read()

    try:
        board = Board()
        board.load_from_text(text)
        game=Game(board)

        commands = extract_commands(text)

        processor = Command(game)
        processor.execute(commands)

    except ValueError as error:
        print("ERROR", error)