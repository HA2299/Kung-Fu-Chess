from position import Position


def test_first_click_selects_piece(game):

    game.click(
        Position(0,0)
    )

    assert game.selected_position == Position(0,0)



def test_second_click_moves_piece(game):

    game.click(
        Position(0,0)
    )

    game.click(
        Position(0,3)
    )

    assert game.board.get_piece(
        Position(0,3)
    ) is not None


    assert game.board.get_piece(
        Position(0,0)
    ) is None