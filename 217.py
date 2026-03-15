# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-15

def get_captured_value(pieces):
    values = {
        "P": 1,
        "R": 5,
        "N": 3,
        "B": 3,
        "Q": 9,
        "K": 0,
    }

    if "K" not in pieces:
        return "Checkmate"

    captured = 39
    for piece in pieces:
        captured -= values[piece]
    return captured
