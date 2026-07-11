from king import King
from position import Position


def test_king_valid_move():

    king = King("W")

    assert king.is_valid_pattern(
        Position(4,4),
        Position(5,5)
    )


def test_king_invalid_move():

    king = King("W")

    assert not king.is_valid_pattern(
        Position(4,4),
        Position(6,6)
    )