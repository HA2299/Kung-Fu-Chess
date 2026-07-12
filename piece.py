from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
        self.color = color


    @property
    @abstractmethod
    def symbol(self):
        pass
    
    @abstractmethod
    def is_valid_pattern(self, start, end):
        pass

    