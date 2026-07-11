from dataclasses import dataclass
from constants import CELL_SIZE

@dataclass(frozen=True)
class Position:
    row: int
    col: int

    @classmethod
    def from_pixels(cls, x: int, y: int):
        return cls(
            row=y // CELL_SIZE,
            col=x // CELL_SIZE
        )