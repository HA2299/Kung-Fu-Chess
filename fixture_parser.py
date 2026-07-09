from constants import COMMANDS_HEADER


def extract_commands(text):
    lines = text.splitlines()

    try:
        start = lines.index(COMMANDS_HEADER) + 1
    except ValueError:
        return []

    commands = []

    for line in lines[start:]:
        line = line.strip()
        if line:
            commands.append(line)

    return commands