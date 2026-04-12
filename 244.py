# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-11

def rook_bishop_attack(rook, bishop):
    if rook[0] == bishop[0] or rook[1] == bishop[1]:
        return "rook"

    for x in [-1, 1]:
        for y in [-1, 1]:
            cell = bishop
            moves = 1
            while moves < 8:
                cell = get_cell(bishop, x*moves, y*moves)
                if not cell:
                    break
                else:
                    if rook == cell:
                        return "bishop"
                    else:
                        moves += 1

    return "neither"


def get_cell(curr, x_dir, y_dir):
    col = ord(curr[0])
    row = int(curr[1])

    new_col = col + x_dir
    new_row = row + y_dir

    if new_col < ord("A") or new_col > ord("H"):
        return False
    elif new_row < 1 or new_row > 8:
        return False
    else:
        return chr(new_col) + str(new_row)
