# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-24

def get_bingo_letter(n):
    bingo = {
        "B": range(1, 16),
        "I": range(16, 31),
        "N": range(31, 46),
        "G": range(46, 61),
        "O": range(61, 76),
    }

    for letter, numbers in bingo.items():
        if n in numbers:
            return letter
