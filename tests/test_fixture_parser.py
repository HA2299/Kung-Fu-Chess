from fixture_parser import extract_commands


def test_extract_commands():

    text = """Board:
wK . .
. . .
Commands:
print board
"""

    commands = extract_commands(text)

    assert commands == [
        "print board"
    ]


def test_no_commands():

    text = """Board:
wK . .
. . .
"""

    commands = extract_commands(text)

    assert commands == []