import sys

from borad import Board
from command import Command
from fixture_parser import extract_commands


def run():
    text = sys.stdin.read()

    try:
        board = Board()
        board.load_from_text(text)

        commands = extract_commands(text)

        processor = Command(board)
        processor.execute(commands)

    except ValueError as error:
        print("ERROR", error)