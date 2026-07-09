from Borad import Board
from commands import Command
from fixture_parser import extract_commands
import sys

text = sys.stdin.read()

try:
    board = Board()
    board.load_from_text(text)

    commands = extract_commands(text)

    processor = Command(board)
    processor.execute(commands)

except ValueError as e:
    print("ERROR", e)