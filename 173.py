# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-30

def find_pawn_moves(position):
    col, row = position
    squares = []

    if row == "8":
        return squares
    else:
        squares.append(col + str(int(row)+1))

    if row == "2":
        squares.append(col + str(int(row)+2))

    return squares
