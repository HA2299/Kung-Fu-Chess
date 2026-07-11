from position import Position


def test_create_position():
    position = Position(2, 3)

    assert position.row == 2
    assert position.col == 3