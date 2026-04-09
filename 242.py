# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-09

def get_next_bingo_number(n):
    bingo = {
        "B": range(1, 16),
        "I": range(16, 31),
        "N": range(31, 46),
        "G": range(46, 61),
        "O": range(61, 76),
    }

    number = int(n[1:])
    new = number + 1

    for letter in bingo:
        if new in bingo[letter]:
            return letter + str(new)

    return "B1"
