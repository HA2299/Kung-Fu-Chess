class Command:
    def __init__(self, board):
        self.board = board

    def execute(self, commands):
        for command in commands:
            self._execute_command(command)

    def _execute_command(self, command):
        if command == "print board":
            print(self.board)