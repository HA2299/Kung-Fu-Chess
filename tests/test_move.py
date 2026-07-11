from move import Move
from position import Position


def test_create_move():

    start = Position(1, 2)
    end = Position(3, 4)

    move = Move(start, end)

    assert move.start == start
    assert move.end == end