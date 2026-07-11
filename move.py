from dataclasses import dataclass

from position import Position

@dataclass(frozen=True)
class Move:
    start: Position
    end: Position