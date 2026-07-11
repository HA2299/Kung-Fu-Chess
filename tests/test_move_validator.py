from move import Move
from position import Position
from move_validator import MoveValidator


def test_valid_piece_move(board):

    validator = MoveValidator()

    move = Move(
        Position(0,0),
        Position(0,3)
    )

    assert validator.is_valid(
        board,
        move
    )


def test_move_without_piece(board):

    validator = MoveValidator()

    move = Move(
        Position(1,1),
        Position(1,2)
    )

    assert not validator.is_valid(
        board,
        move
    )