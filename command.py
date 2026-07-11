from constants import CELL_SIZE
from position import Position


class Command:
    def __init__(self, board,game):
        self.board = board
        self.game=game

    def execute(self, commands):
        for command in commands:
            self._execute_command(command)

    def _execute_command(self, command):
        if command == "print board":
            print(self.board)
        elif command.startswith("click"):
            self._execute_click(command)
        elif command.startswith("wait"):
            pass
            # self._execute_wait(command)
    
    def _execute_click(self, command):
        _, x, y = command.split()
    
        x = int(x)
        y = int(y)
    
        position = Position.from_pixels(x, y)

        self.game.click(position)    
        
    # def _execute_wait(self, command):
    #     _, seconds = command.split()
    #     self.board.wait(int(seconds))
