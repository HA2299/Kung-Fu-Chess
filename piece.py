from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def is_valid_move(self, start, end):
        pass